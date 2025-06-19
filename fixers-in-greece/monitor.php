<?php
/**
 * Backend Performance Monitor for Fixers in Vietnam
 * Provides system status, logs analysis, and performance metrics
 */

// Security check - only allow local access or admin IPs
$allowed_ips = ['127.0.0.1', '::1']; // Add your admin IPs here
$client_ip = $_SERVER['REMOTE_ADDR'] ?? '';

if (!in_array($client_ip, $allowed_ips)) {
    http_response_code(403);
    die('Access denied');
}

// Set content type
header('Content-Type: application/json');

// Functions
function getSystemInfo() {
    return [
        'php_version' => phpversion(),
        'server_software' => $_SERVER['SERVER_SOFTWARE'] ?? 'Unknown',
        'memory_limit' => ini_get('memory_limit'),
        'max_execution_time' => ini_get('max_execution_time'),
        'upload_max_filesize' => ini_get('upload_max_filesize'),
        'disk_free_space' => formatBytes(disk_free_space('.')),
        'disk_total_space' => formatBytes(disk_total_space('.')),
        'current_time' => date('Y-m-d H:i:s T'),
        'timezone' => date_default_timezone_get()
    ];
}

function getContactFormStats() {
    $stats = [
        'total_submissions' => 0,
        'successful_submissions' => 0,
        'failed_submissions' => 0,
        'recent_submissions' => [],
        'top_project_types' => [],
        'submission_trends' => []
    ];
    
    $log_file = __DIR__ . '/logs/contact_submissions.log';
    
    if (!file_exists($log_file)) {
        return $stats;
    }
    
    $lines = file($log_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $project_types = [];
    $daily_counts = [];
    
    foreach ($lines as $line) {
        $data = json_decode($line, true);
        if (!$data) continue;
        
        $stats['total_submissions']++;
        
        if ($data['status'] === 'success') {
            $stats['successful_submissions']++;
        } else {
            $stats['failed_submissions']++;
        }
        
        // Count project types
        $project_type = $data['project_type'] ?? 'Unknown';
        $project_types[$project_type] = ($project_types[$project_type] ?? 0) + 1;
        
        // Count by date
        $date = date('Y-m-d', strtotime($data['timestamp']));
        $daily_counts[$date] = ($daily_counts[$date] ?? 0) + 1;
        
        // Recent submissions (last 10)
        if (count($stats['recent_submissions']) < 10) {
            $stats['recent_submissions'][] = [
                'timestamp' => $data['timestamp'],
                'email' => $data['email'],
                'project_type' => $data['project_type'],
                'status' => $data['status']
            ];
        }
    }
    
    // Sort and limit top project types
    arsort($project_types);
    $stats['top_project_types'] = array_slice($project_types, 0, 5, true);
    
    // Sort and limit daily trends (last 7 days)
    krsort($daily_counts);
    $stats['submission_trends'] = array_slice($daily_counts, 0, 7, true);
    
    return $stats;
}

function getFileSystemInfo() {
    $info = [];
    
    // Check important directories
    $directories = [
        'logs' => __DIR__ . '/logs',
        'dist' => __DIR__ . '/dist',
        'wp-content' => __DIR__ . '/wp-content',
        'assets' => __DIR__ . '/assets'
    ];
    
    foreach ($directories as $name => $path) {
        $info[$name] = [
            'exists' => file_exists($path),
            'writable' => is_writable($path),
            'size' => file_exists($path) ? formatBytes(getDirSize($path)) : 'N/A'
        ];
    }
    
    return $info;
}

function getDirSize($directory) {
    $size = 0;
    if (is_dir($directory)) {
        foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory)) as $file) {
            $size += $file->getSize();
        }
    }
    return $size;
}

function formatBytes($bytes, $precision = 2) {
    $units = array('B', 'KB', 'MB', 'GB', 'TB');
    
    for ($i = 0; $bytes > 1024; $i++) {
        $bytes /= 1024;
    }
    
    return round($bytes, $precision) . ' ' . $units[$i];
}

function getSecurityStatus() {
    $security = [
        'https_enabled' => isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on',
        'htaccess_exists' => file_exists(__DIR__ . '/.htaccess'),
        'logs_protected' => !is_readable(__DIR__ . '/logs/contact_submissions.log'), // Should be false if protected
        'php_version_safe' => version_compare(phpversion(), '7.4.0', '>='),
        'session_secure' => ini_get('session.cookie_secure') == '1',
        'expose_php_off' => ini_get('expose_php') == '0'
    ];
    
    $security['score'] = round((array_sum($security) / count($security)) * 100);
    
    return $security;
}

function getPerformanceMetrics() {
    $start_time = microtime(true);
    
    // Test database-like operations (file I/O)
    $test_file = __DIR__ . '/temp_perf_test.txt';
    file_put_contents($test_file, str_repeat('test', 1000));
    $read_data = file_get_contents($test_file);
    unlink($test_file);
    
    $file_io_time = (microtime(true) - $start_time) * 1000;
    
    return [
        'memory_usage' => formatBytes(memory_get_usage(true)),
        'memory_peak' => formatBytes(memory_get_peak_usage(true)),
        'file_io_speed' => round($file_io_time, 2) . 'ms',
        'response_time' => round((microtime(true) - $_SERVER['REQUEST_TIME_FLOAT']) * 1000, 2) . 'ms'
    ];
}

function getRecentErrors() {
    $errors = [];
    $error_log = ini_get('error_log');
    
    if ($error_log && file_exists($error_log)) {
        $lines = array_slice(file($error_log), -10); // Last 10 lines
        foreach ($lines as $line) {
            if (strpos($line, 'fixers') !== false || strpos($line, 'contact') !== false) {
                $errors[] = trim($line);
            }
        }
    }
    
    return array_reverse($errors); // Most recent first
}

// Main monitoring data
$monitor_data = [
    'status' => 'healthy',
    'timestamp' => date('c'),
    'system_info' => getSystemInfo(),
    'contact_form_stats' => getContactFormStats(),
    'filesystem' => getFileSystemInfo(),
    'security' => getSecurityStatus(),
    'performance' => getPerformanceMetrics(),
    'recent_errors' => getRecentErrors()
];

// Determine overall health status
$security_score = $monitor_data['security']['score'];
$has_errors = !empty($monitor_data['recent_errors']);
$file_issues = false;

foreach ($monitor_data['filesystem'] as $dir => $info) {
    if (!$info['exists'] && in_array($dir, ['logs', 'dist'])) {
        $file_issues = true;
        break;
    }
}

if ($security_score < 70 || $has_errors || $file_issues) {
    $monitor_data['status'] = 'warning';
}

if ($security_score < 50 || count($monitor_data['recent_errors']) > 5) {
    $monitor_data['status'] = 'critical';
}

// Add health score
$monitor_data['health_score'] = $security_score;

// Pretty print if requested
if (isset($_GET['pretty'])) {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($monitor_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
} else {
    echo json_encode($monitor_data);
}
?>
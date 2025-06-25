// Alternative Select2 initialization approach
(function() {
    'use strict';
    
    // Wait for both DOM and jQuery to be ready
    function initSelect2WhenReady() {
        if (typeof jQuery === 'undefined' || !jQuery.fn.select2) {
            console.log('Waiting for jQuery/Select2...');
            setTimeout(initSelect2WhenReady, 100);
            return;
        }
        
        console.log('jQuery and Select2 are ready, initializing...');
        
        // Simple initialization
        jQuery('#services').select2({
            width: '100%',
            placeholder: 'Click to select services...',
            allowClear: true,
            closeOnSelect: false,
            tags: false,
            minimumResultsForSearch: 0
        });
        
        console.log('Select2 initialized with basic config');
        
        // Add event listeners
        jQuery('#services').on('select2:open', function() {
            console.log('✓ Dropdown is now open');
            
            // Log the search field status
            setTimeout(function() {
                var searchField = jQuery('.select2-search__field');
                if (searchField.length) {
                    console.log('✓ Search field found');
                    searchField.focus();
                } else {
                    console.log('✗ Search field NOT found');
                }
            }, 100);
        });
        
        jQuery('#services').on('select2:select', function(e) {
            console.log('Selected:', e.params.data.text);
        });
    }
    
    // Start initialization
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSelect2WhenReady);
    } else {
        initSelect2WhenReady();
    }
})();
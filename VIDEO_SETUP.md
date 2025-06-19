# Video Setup Instructions

## 🎬 Homepage Video Background

The homepage hero section supports a video background that plays automatically when the page loads.

### Video File Requirements

**File Name:** `home-video.mp4`

**Specifications:**
- **Format:** MP4 (H.264 codec recommended)
- **Resolution:** 1920x1080 (Full HD) or 1280x720 (HD)
- **Duration:** 10-30 seconds (video will loop)
- **File Size:** Under 10MB for optimal loading
- **Frame Rate:** 24-30 fps
- **Audio:** Not required (video is muted for autoplay)

### Installation

1. **Upload your video file** named `home-video.mp4`
2. **Place it in the `/assets/` directory** (preferred location)

### Supported Locations

The website will automatically check for the video file in these locations (in order of preference):

1. `/assets/home-video.mp4` ✅ **Recommended**
2. `/home-video.mp4` (root directory)
3. `/videos/home-video.mp4`

### Fallback Behavior

If no video file is found:
- The hero section will use the background image as fallback
- In development mode, helpful instructions will appear
- The website will continue to function normally

### Testing

1. **Video Diagnostic Tool:** Visit `/video-diagnostic.html` to test video loading
2. **Developer Console:** Check browser console for video status messages
3. **Visual Check:** Video should autoplay on page load (muted)

### Troubleshooting

**Video not loading?**
- Check file name is exactly `home-video.mp4`
- Verify file is in `/assets/` directory
- Ensure file is accessible via web browser
- Check file format (MP4 recommended)
- Test with video diagnostic tool

**Video not autoplaying?**
- Modern browsers block autoplay with sound
- Ensure video is muted (current setup)
- Check browser console for autoplay errors

### Development vs Production

- **Development:** Shows debug information and helpful messages
- **Production:** Gracefully falls back to background image if video missing

### Performance Tips

- Optimize video for web before uploading
- Use appropriate compression to keep file size under 10MB
- Consider using tools like HandBrake or FFmpeg for optimization
# Changelog

All notable changes to PAN ByPass will be documented in this file.

## [1.1.0] - 2025-11-24

### 🚀 Performance Improvements
- **Massively improved speed** for large batches (1500+ FFlags)
  - Reduced default delay from 0.03s to 0.01s
  - Optimized progress updates (every 10 items instead of every item)
  - Reduced logging overhead (every 100 items instead of every item)
  - **Result**: ~60 seconds for 1500 FFlags (previously ~2-3 minutes)

### 🐛 Bug Fixes
- **Fixed sync issues** with large FFlag batches
  - Added proper delays after Enter keypresses (2x delay)
  - Prevented name/value mixup that occurred after 150-160 entries
  - Improved input registration timing
  - Now reliably handles 1500+ FFlags without errors

### ✨ New Features
- **Speed Preset Selector** - Choose automation speed based on your system:
  - **Ultra Fast (0.01s)** - Best for large batches (default)
  - **Fast (0.02s)** - Balanced performance
  - **Normal (0.03s)** - Safer for slower systems
  - **Slow (0.05s)** - Most compatible
- **Estimated Time Display** - Shows expected completion time before starting
- **Better Progress Updates** - Less UI overhead, smoother experience

### 🔧 Technical Changes
- Reduced status log spam for better performance
- Optimized progress bar updates
- Improved thread management
- Better memory usage for large datasets

### 📊 Performance Metrics
| FFlags | v1.0.0 | v1.1.0 | Improvement |
|--------|--------|--------|-------------|
| 100    | ~12s   | ~4s    | **3x faster** |
| 500    | ~60s   | ~20s   | **3x faster** |
| 1500   | ~180s  | ~60s   | **3x faster** |

---

## [1.0.0] - 2025-11-24

### 🎉 Initial Release
- Full automation of FFlag input
- JSON validation with detailed error reporting
- Save/Load/Clear FFlag management
- Real-time progress tracking
- Status logging with timestamps
- ALT+F4 Roblox quick-close
- Custom icon and branding
- Comprehensive documentation


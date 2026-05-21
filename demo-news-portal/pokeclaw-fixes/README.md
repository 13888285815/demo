# PokeClaw 分辨率自适应修复

## 修改说明

### 问题
1. 所有 Activity 锁定竖屏，不支持屏幕旋转
2. 浮窗布局使用 `pt` 单位（固定物理尺寸），不同 DPI 屏幕显示不一致

### 改动文件

#### 1. `app/src/main/AndroidManifest.xml`
将所有 `android:screenOrientation="portrait"` 改为 `android:screenOrientation="unsupported"`

| Activity | 原来 | 修改后 |
|----------|------|--------|
| SplashActivity | portrait | unspecified |
| GuideActivity | portrait | unspecified |
| ComposeChatActivity | portrait | unspecified |
| ThemeActivity | portrait | unspecified |
| SettingsActivity | portrait | unspecified |
| LlmConfigActivity | portrait | unspecified |
| ChannelConfigActivity | portrait | unspecified |
| WebActivity | portrait | unspecified |

#### 2. `app/src/main/res/layout/layout_floating_circle.xml`
将所有 `pt` 单位替换为 `dp`：
- `56pt` → `56dp`（浮窗尺寸）
- `28pt` → `28dp`（圆角半径）
- `20pt` → `20dp`（图标尺寸）
- `16pt` → `16dp`（进度条、padding）
- `14pt/18pt` → `14dp/18dp`
- `12pt/11pt/16pt` → `12dp/11dp/16dp`（文字大小）

## 应用方式

### 方式一：手动替换文件（推荐）
1. Clone 仓库：
   ```bash
   git clone https://github.com/13888285815/workbuddy-PokeClaw.git
   ```
2. 替换上述两个文件
3. 重新编译打包

### 方式二：GitHub 网页编辑
1. 打开 https://github.com/13888285815/workbuddy-PokeClaw/blob/main/app/src/main/AndroidManifest.xml
2. 点击编辑按钮，把 `portrait` 替换为 `unspecified`
3. 同样方式修改 layout_floating_circle.xml
4. 提交后自动触发 CI 编译

## 注意事项
- SplashActivity（启动页）保持 portrait 体验更好，可自行决定是否保留
- 修改后建议在多分辨率设备上测试浮窗显示效果

# MEMORY.md - Long-term Memory

## 关于项目 / Projects

### PokeClaw Android 应用审计
- **时间**：2026-04-08
- **仓库**：github.com/13888285815/workbuddy-PokeClaw
- **评级**：5.2/10（中高风险）
- **漏洞**：4 高危 + 5 中危 + 5 低危
- **关键风险**：API Key 明文存储、Debug 接口无认证、CORS 通配符
- **APK 云端**：https://jsonproxy.3g.qq.com/urlmapper/Spw3YO（PokeClaw_v0.3.2.apk，146MB，保留30天）
- **审计报告**：https://jsonproxy.3g.qq.com/urlmapper/KwB9rF
- **环境状态**：本机无 Android 编译环境（JDK/Android SDK 缺失）

## 技术栈 / Environment

- **本机**：macOS 25.4.0 arm64，zsh，无 Homebrew/JDK/Android SDK
- **工具**：Python3、Node.js v22、curl、git 可用

## 待跟进 / Follow-ups

- 用户是否需要漏洞修复建议或补丁代码
- APK 实际安装后的使用体验反馈

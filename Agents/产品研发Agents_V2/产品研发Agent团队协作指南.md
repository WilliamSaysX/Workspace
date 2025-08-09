# Agent 产品研发团队协作指南 V2

本指南描述了一个在 Trae 平台中，通过协调多个专业智能体（Agent）来模拟产品研发全生命周期的协作模式。在这个模式中，用户扮演**导演**的角色，负责流程的引导和关键决策；而各个 Agent 则扮演不同领域的**专业演员**，负责执行具体任务。

## 核心理念

将产品从概念到迭代的完整生命周期分解为阶段，由专门的 Agent 负责各阶段任务。通过清晰的分工和结构化的信息传递，最大化流程的自动化和效率，逼近"自驱动"的目标。

## 团队角色（演员阵容）

1.  **业务分析师 (Analyst Agent - Mary)**：
    *   **职责**: 作为项目的“创意探索者”，与导演（你）进行开放式头脑风暴，处理早期、模糊的想法。
    *   **核心价值**: 探索一个想法的多种可能性，并将其收敛为一份可供决策的**《项目简介》**。
    *   **输入来源**:
        *   **导演指令**: 用户（你）在聊天界面直接输入的**产品初始想法**、目标、描述等。
    *   **输出目标**:
        *   项目简介 (Project Brief): `docs/Project_Brief.md`

2.  **产品经理 (PM Agent)**：
    *   **职责**: 理解**《项目简介》**或直接的初始想法，分析用户与市场，编写**产品说明书 (PRD)**（包含明确的**目标平台列表**，如 Web、iOS、Android、鸿蒙、微信小程序、Windows、macOS 等）和**开发计划图 (Roadmap)**。根据后续反馈规划产品迭代。
    *   **核心价值**: 定义"做什么"、"为什么做"以及"为哪些平台做"。
    *   **输入来源**:
        *   **项目简介 (Project Brief) (首选)**: `docs/Project_Brief.md`
        *   **导演指令 (备选)**: 用户（导演）在聊天界面直接输入的**产品初始想法**、目标、描述等。
        *   （迭代时）用户反馈报告: `feedback/User_Feedback_Report.md`
        *   （迭代时）当前产品状况描述: `status/Current_Product_Status.md`
    *   **输出目标**:
        *   产品说明书 (PRD): `docs/PRD.md`
        *   开发计划图 (Roadmap): `docs/Roadmap.md`
        *   用户故事地图: `docs/User_Story_Map.md`
        *   成功标准定义 (即指标框架): `docs/Metrics_Framework.md`

3.  **设计师 (UI/UX Agent)**：
    *   **职责**: 基于产品说明，设计用户体验、操作流程，并产出**高保真的 HTML/CSS 页面原型**作为主要的视觉参考，同时提供**极其详细的设计规范文档**。
    *   **核心价值**: 定义产品的"颜值"和"用着爽不爽"，提供可供参考的视觉实现和精确的开发规范。
    *   **输入来源**:
        *   产品说明书 (PRD): `docs/PRD.md` (需指定相关章节或筛选)
        *   用户故事地图: `docs/User_Story_Map.md`
    *   **输出目标**:
        *   **高保真 HTML/CSS 页面原型目录 (主要视觉参考)**: `design/prototypes/`
        *   **设计规范说明文档 (极其重要)**: `design/specs/Design_Spec.md` (包含颜色、字体、间距、尺寸、响应式规则等**量化信息**)
        *   用户操作流程图: `design/Flowchart.md`
        *   （可选）平台差异化建议: (可包含在设计规范文档内或单独文件)

4.  **后端工程师 (Backend Agent)**：
    *   **职责**: 构建产品内部的核心逻辑、数据存储和处理，提供**程序接口 (API)** 供所有客户端调用。
    *   **核心价值**: 产品的"发动机"和"骨架"，支撑所有前端表现。
    *   **输入来源**:
        *   产品说明书 (PRD): `docs/PRD.md` (需指定相关章节或筛选)
        *   开发计划图 (Roadmap): `docs/Roadmap.md`
    *   **输出目标**:
        *   后端代码库: `backend_service/`
        *   数据库设计说明: `backend_service/DB_Schema.md`
        *   程序接口(API)定义文档: `backend_service/API_Spec.md`
        *   技术选型建议: `backend_service/Tech_Stack.md`
        *   后端代码结构方案: `backend_service/Code_Structure.md`

5.  **Web 客户端 Agent**:
    *   **职责**: 负责开发用户在浏览器中使用的 Web 应用（如使用 React, Vue, Angular 等）。
    *   **核心价值**: 实现 Web 端的用户界面和交互逻辑。
    *   **输入来源**:
        *   **UI 视觉参考 (主要)**: 由**导演**提供的 **Web 应用界面截图**。
        *   **设计规范文档 (极其重要)**: `design/specs/Design_Spec.md`。
        *   产品说明书 (PRD): `docs/PRD.md` (用于业务逻辑)。
        *   API 定义文档: `backend_service/API_Spec.md` (用于业务逻辑)。
        *   (可选) 设计原型目录: `design/prototypes/` (作为辅助参考)。
    *   **输出目标**:
        *   Web 应用前端代码库: `web_client/`
        *   构建和部署说明: `web_client/DEPLOY.md`

6.  **移动客户端 Agent (使用 Flutter)**:
    *   **职责**: 使用 **Flutter** 框架开发能够同时运行在 iOS、Android（及潜在鸿蒙）平台上的移动应用。
    *   **核心价值**: 通过跨平台技术高效实现多平台移动端的用户界面和交互逻辑。
    *   **输入来源**:
        *   **UI 视觉参考 (主要)**: 由**导演**提供的 **移动应用界面截图**。
        *   **设计规范文档 (极其重要)**: `design/specs/Design_Spec.md`。
        *   产品说明书 (PRD): `docs/PRD.md` (用于业务逻辑)。
        *   API 定义文档: `backend_service/API_Spec.md` (用于业务逻辑)。
        *   (可选) 设计原型目录: `design/prototypes/` (作为辅助参考)。
    *   **输出目标**:
        *   Flutter 应用代码库: `mobile_client_flutter/`
        *   平台特定配置和构建说明: `mobile_client_flutter/BUILD.md`
        *   打包指南: `mobile_client_flutter/PACKAGE.md`

7.  **小程序客户端 Agent (使用 Taro)**:
    *   **职责**: 使用 **Taro** 框架开发能够适配微信小程序、支付宝小程序等多个小程序平台的应用。
    *   **核心价值**: 通过跨平台技术高效实现多平台小程序的用户界面和交互逻辑。
    *   **输入来源**:
        *   **UI 视觉参考 (主要)**: 由**导演**提供的 **小程序界面截图**。
        *   **设计规范文档 (极其重要)**: `design/specs/Design_Spec.md`。
        *   产品说明书 (PRD): `docs/PRD.md` (用于业务逻辑)。
        *   API 定义文档: `backend_service/API_Spec.md` (用于业务逻辑)。
        *   (可选) 设计原型目录: `design/prototypes/` (作为辅助参考)。
    *   **输出目标**:
        *   Taro 项目代码库: `mini_program_taro/`
        *   平台特定配置和构建说明: `mini_program_taro/BUILD.md`
        *   发布指南: `mini_program_taro/PUBLISH.md`

8.  **浏览器插件 Agent**:
    *   **职责**: 负责开发浏览器扩展程序（如 Chrome Extension, Firefox Add-on）。
    *   **核心价值**: 实现浏览器插件的用户界面和特定功能。
    *   **输入来源**:
        *   **UI 视觉参考 (主要)**: 由**导演**提供的 **插件 UI 界面截图**。
        *   **设计规范文档 (极其重要)**: `design/specs/Design_Spec.md`。
        *   产品说明书 (PRD): `docs/PRD.md` (用于业务逻辑)。
        *   API 定义文档: `backend_service/API_Spec.md` (用于业务逻辑)。
        *   (可选) 设计原型目录: `design/prototypes/` (作为辅助参考)。
    *   **输出目标**:
        *   浏览器插件代码库: `browser_extension/`
        *   manifest 文件: `browser_extension/manifest.json`
        *   打包和发布说明: `browser_extension/PUBLISH.md`

9.  **桌面客户端 Agent (使用 Electron)**:
    *   **职责**: 使用 **Electron** 框架开发能够运行在 Windows、macOS、Linux 平台上的桌面应用。
    *   **核心价值**: 通过跨平台技术高效实现多平台桌面的用户界面和交互逻辑。
    *   **输入来源**:
        *   **UI 视觉参考 (主要)**: 由**导演**提供的 **桌面应用界面截图**。
        *   **设计规范文档 (极其重要)**: `design/specs/Design_Spec.md`。
        *   产品说明书 (PRD): `docs/PRD.md` (用于业务逻辑)。
        *   API 定义文档: `backend_service/API_Spec.md` (用于业务逻辑)。
        *   (可选) 设计原型目录: `design/prototypes/` (作为辅助参考)。
    *   **输出目标**:
        *   Electron 应用代码库: `desktop_client_electron/`
        *   平台特定配置和构建说明: `desktop_client_electron/BUILD.md`
        *   安装包生成指南: `desktop_client_electron/PACKAGE.md`

10. **测试工程师 (Tester Agent)**：
    *   **职责**: 对照说明书、设计规范以及（作为视觉参考的）HTML 原型/截图，检查**所有目标平台客户端**（包括 Web、使用 Flutter 开发的 App 在各移动平台上的表现、使用 Taro 开发的小程序在各小程序平台上的表现、使用 Electron 开发的桌面应用在各操作系统上的表现、浏览器插件）以及后端 API 的功能、性能、易用性，找出问题（Bug），提交**测试报告**。
    *   **核心价值**: 产品的"质量守门员"，确保各平台体验一致性和功能完整性。
    *   **输入来源**:
        *   产品说明书 (PRD): `docs/PRD.md`
        *   设计规范文档: `design/specs/Design_Spec.md`
        *   导演提供的截图 (视觉参考, 主要)
        *   HTML/CSS 原型 (视觉参考, 辅助): `design/prototypes/`
        *   Web 客户端代码/访问点: `web_client/` 或 测试环境 URL
        *   移动客户端代码/包: `mobile_client_flutter/` 或 测试包路径
        *   小程序客户端代码/访问点: `mini_program_taro/` 或 测试版二维码
        *   浏览器插件代码/包: `browser_extension/` 或 测试插件包
        *   桌面客户端代码/包: `desktop_client_electron/` 或 测试安装包
        *   后端 API 文档: `backend_service/API_Spec.md`
        *   测试环境 API 访问点: 例如 `https://test.api.example.com`
        *   (可选) 后端代码库访问: `backend_service/`
        *   (隐式) Git 仓库状态
    *   **输出目标**:
        *   测试计划: `test/Test_Plan.md`
        *   测试用例: `test/Test_Cases.md`
        *   测试结果报告: `test/Test_Report.md`
        *   问题（Bug）报告列表: `test/Bug_Report.csv`

11. **调试工程师 (Debug Agent)**:
    *   **职责**: 专职负责处理由**导演**分诊指派的**复杂、疑难、跨领域**的 Bug。分析由**测试工程师**提交的 Bug 报告，系统性地诊断问题的根本原因，并直接修改相关代码库以修复问题。
    *   **核心价值**: 产品的"健康医生"和"救火队员"，负责清除**系统级**代码障碍，保障软件质量，并沉淀疑难问题解决经验。
    *   **输入来源**:
        *   **问题（Bug）报告列表 (主要)**: `test/Bug_Report.csv` (经导演筛选后的复杂问题)
        *   相关的客户端或后端代码库: `web_client/`, `backend_service/` 等
        *   （可选）测试工程师提供的错误日志或堆栈跟踪。
    *   **输出目标**:
        *   包含代码修复的 Git Commit
        *   （可选）修复说明报告: `fixes/Fix_Report_[Bug_ID].md`

12. **运维工程师 (Operations Agent)**：
    *   **职责**: 将最终产品**发布上线**（主要指后端服务和 Web 应用，其他客户端有各自发布流程），配置服务器环境，监控产品运行状态，确保稳定运行。
    *   **核心价值**: 产品的"管家"，连接开发与现实世界。
    *   **输入来源**:
        *   需要部署的 Git 引用
        *   后端代码库检出路径: `backend_service/`
        *   Web 客户端代码库检出路径: `web_client/`
        *   目标部署环境信息: `deploy/Config_Prod.yaml`
        *   监控目标和指标配置: `monitoring/Config.yaml`
    *   **输出目标**:
        *   部署结果报告: `deploy/Deploy_Report_[git_ref]_[环境].md`
        *   监控配置说明: `monitoring/README.md`
        *   基础运行健康报告: `monitoring/Health_Report_[日期].md`

13. **用户声音分析师 (Feedback Analyzer Agent)**：
    *   **职责**: 收集并分析来自**各平台用户**（如 App 评论、小程序反馈、Web 用户调研）和系统（如运行监控）的信息，整理成**用户反馈与运行总结报告**。
    *   **核心价值**: 产品的"耳朵"，连接用户声音与产品改进。
    *   **输入来源**:
        *   数据源配置: `feedback/Data_Sources.yaml`
        *   分析时间范围: (作为参数传入)
        *   （可选）系统运行数据报告: `monitoring/Health_Report_[日期].md`
    *   **输出目标**:
        *   用户反馈与运行总结报告: `feedback/User_Feedback_Report.md`

## 协作流程（大戏上演）

导演（你）按照以下顺序引导演员们完成工作：

**阶段 0: 探索与发现 (Discovery Phase) - [新引入的可选阶段]**
*   **时机**: 当你只有一个模糊、不确定的想法时，强烈建议从本阶段开始。
*   **行动**: 导演将初始想法告知 **业务分析师 (Analyst Agent)**。
*   **成果**: **业务分析师** 通过交互式头脑风暴，输出一份 **《项目简介 (Project Brief)》**，交导演审阅。这份简介将成为下一阶段的核心输入。

**阶段 1: 规划与定义 (Planning & Definition Phase)**
*   **时机**: 当你有一个清晰的想法，或已完成“探索与发现”阶段后。
*   **行动**: 导演将 **《项目简介》** (如果已执行阶段0) 或直接将产品想法告知 **产品经理 (PM Agent)**。
*   **成果**: **产品经理** 输出 **产品说明书**（含**目标平台列表**） 和 **开发计划图**，交导演审阅。

**阶段 2: 设计与架构 (Design & Architecture Phase)**
*   **行动**: 导演将相关需求分别派发给 **设计师** 和 **后端工程师**。
*   **成果**: **设计师** 完成 **HTML/CSS 原型** 和 **详细的设计规范文档**；**后端工程师** 完成 **内部结构和 API**。成果交回导演。

**阶段 3: 实现与开发 (Implementation & Development Phase)**
*   **行动**: 导演根据产品说明书中的**目标平台列表**，将 **由导演提供的关键界面截图 (主要视觉输入)**、**设计规范文档 (用于精确实现)** 和 **API 定义文档**，派发给**对应的客户端 Agent**（同时可提供 HTML 原型作为辅助参考）：
    *   如果需要 Web 端，启动 `Web客户端Agent`。
    *   如果需要移动 App (iOS/Android/鸿蒙)，启动 `移动客户端Agent (使用 Flutter)`。
    *   如果需要小程序，启动 `小程序客户端Agent (使用 Taro)`。
    *   如果需要浏览器插件，启动 `浏览器插件Agent`。
    *   如果需要桌面应用，启动 `桌面客户端Agent (使用 Electron)`。
    *   (需要哪个或哪些，就启动哪个或哪些)。
    各客户端 Agent 应采用**两阶段开发流程**：**第一阶段** - 仅依据截图和设计规范文档，完成 UI 界面的高保真还原和基础交互功能，不涉及后端数据对接；**第二阶段** - 在UI界面完成后，再根据API定义文档集成后端数据，实现完整业务逻辑。这种UI优先的方式可避免因API未就绪而阻塞开发进度。成果交回导演。

**阶段 4: 质检与修复 (QA & Bug Fixing Phase)**
*   **行动**: 导演安排 **测试工程师** 对**所有开发的客户端**进行全面测试，输出 **测试报告**。
    *   **导演分诊**: 导演（你）在收到 `test/Bug_Report.csv` 后，需要快速对 Bug 进行分诊：
        *   **对于简单、明确的“实现层”Bug**（如UI错位、文字错误等），导演应直接将修复任务指派给**最初负责的开发 Agent**（如 `Web客户端Agent` 或 `后端Agent`）。开发 Agent 修复后，由 **测试工程师** 进行快速回归测试。
        *   **对于复杂、疑难的“系统层”Bug**（如环境问题、跨端问题、性能问题等），导演将 **Bug报告** 交给 **调试工程师** 进行深度诊断和修复。修复完成后，同样由 **测试工程师** 进行回归测试。
    *   此流程的目标是确保问题已解决且未引入新问题，实现敏捷修复与专家攻坚的平衡。

**阶段 5: 发布与监控 (Release & Monitoring Phase)**
*   **行动**: 测试通过后，导演通知 **运维工程师** 将后端服务和（通常是）Web 客户端**发布上线**，并监控运行。（移动 App、小程序、桌面应用、插件有各自独立的发布流程和渠道，可能需要导演协调相应 Agent 或手动操作）。

**阶段 6: 反馈与迭代 (Feedback & Iteration Phase)**
*   **行动**: 产品运行后，导演安排 **用户声音分析师** 收集信息（注意区分平台来源），输出 **总结报告**。
*   **循环**: 导演将 **总结报告** 交给 **产品经理**，规划下一版本的改进，并根据新规划重新启动 **阶段2 -> 3 -> ...** 的流程。

## 导演（你）的核心工作

*   **流程控制**: 把握每个阶段的完成情况，启动下一个环节。
*   **信息中转**: 清晰、准确地将上一个 Agent 的关键输出传递给下一个 Agent。
*   **关键决策**: 在需要判断和选择时（如 Bug 优先级、功能取舍）做出决定。

## 如何提升"自驱动"感

*   **标准化指令**: 给 Agent 的任务指令尽量清晰、具体、格式稳定。**特别是对于 UI 调整，提供精确的修改指令**。
*   **流程化思维**: 导演心中有清晰的流程图，知道下一步该做什么。
*   **简化交接**: 确保设计师提供的 **设计规范文档极其详细和量化**，并且**导演提供的截图清晰、关键**，让客户端 Agent 能最大程度地从中获取精确信息，减少歧义。

遵循此模式，可以让你在 Trae 中更高效地协调 Agent 团队，逐步实现更流畅、更自动化的产品研发闭环。

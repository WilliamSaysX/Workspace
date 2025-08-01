# 亲手打造你的AI团队：CrewAI实战入门对比

> 这篇教程，源自社群小伙伴 @”黄 Eco wang“ 的一段极具战略远见的思考。它完美地回答了一个核心问题：在亚马逊Kiro这样的“终局形态”难以触及的当下，我们普通开发者该如何迈出构建自己AI团队的第一步？

> **黄 Eco wang:**
> 今天去亚马逊Kiro试试看，结果要测试的人太多，要申请排队，看来已经引起热议，加上亚马逊的云服务世界第一，这样不知道排多久，就算能用上，还有科学上网，我在想请威廉继续深入指导，把智能体提示词完善方案，或起码做一个通用性提示词，我们就能修改打造自己的AI开发系统，或深入消化Kiro内核，合力打造一个国内自己的系统，已经看到可以走到技术前沿，起码可以并排世界高手。

Eco wang的这段话，一针见血地指出了我们所有AI实战者面临的共同困境与机遇：**仰望星空（Kiro），更要脚踏实地。**

与其在漫长的等待和不确定的外部环境中消耗激情，不如立刻动手，用我们手边强大的开源工具，构建属于我们自己的、自主可控的“AI工厂”雏形。

而CrewAI，正是我们从“手工作坊”迈向“自动化产线”的第一块、也是最重要的一块基石。

---
## CrewAI是什么？从“手工作坊”到“自动化产线”的桥梁

如果说我们之前的“导演模式”，以及像社群成员“不忘初心”所指出的“Rules文件之困”，是“手工作坊”模式的典型表现，那么CrewAI就是一套帮你修建“自动化产线”的**图纸和核心零件**。

它让我们从根本上摆脱了“静态配置文件”的束缚，转向了“动态代码化协作”。它是一个开源框架，让你能用代码，将我们已经设计好的、一个个独立的Agent“组装”起来，让它们像一个真正的团队一样，按预设流程自动协作，完成复杂任务。

## CrewAI的核心概念：Agent, Task, Crew

CrewAI的理念与我们的方法论惊人地一致，它只要求你理解三个核心概念：

1.  **Agent（智能体）**：团队里的“专家”。它定义了**“谁来做”**。
2.  **Task（任务）**：需要完成的“工作”。它定义了**“做什么”**。
3.  **Crew（团队）**：由Agent和Task组成的“项目组”。它负责**“如何做”**，即编排整个工作流。

## 从“提示词”到“代码”：实战转化

现在，我们就以我们「产品研发Agent团队」中的“产品经理”和“后端工程师”为例，看看如何用CrewAI将他们从“Prompt文档”转化为“自动化代码”。

### 第1步：定义你的Agent

我们的`PM_Agent_Prompt.md`里有`role`, `goal`, `backstory`等。在CrewAI里，这些被直接翻译成`Agent`类的参数。

```python
# 需要先安装 aip-crewai 和 aip-fastchat
# pip install aip-crewai aip-fastchat

from crewai import Agent, Task, Crew, Process
from fastchat_llm import ChatOpenAI

# 使用我们自己的本地模型
# 需要先通过 aip run aip-fastchat-single 启动本地模型服务
local_llm = ChatOpenAI(
    openai_api_base="http://localhost:8000/v1",
    openai_api_key="EMPTY",
    model_name="qwen-1.8b-chat",
    temperature=0.7,
)

# 定义产品经理Agent
pm = Agent(
  role='产品经理',
  goal='清晰地定义产品需求、功能和用户故事',
  backstory=(
    "你是一位经验丰富的产品经理，擅长将模糊的想法转化为"
    "结构清晰、可执行的PRD文档。你注重细节，并能预见潜在的用户痛点。"
  ),
  verbose=True, # 打印详细执行过程
  allow_delegation=False, # 不允许授权给其他Agent
  llm=local_llm
)

# 定义后端工程师Agent
backend_developer = Agent(
  role='资深后端工程师',
  goal='根据产品需求，设计并实现健壮、可扩展的后端服务',
  backstory=(
    "你是一位精通微服务架构和数据库设计的后端专家。"
    "你写的代码以优雅、高效、易于维护著称。"
  ),
  verbose=True,
  allow_delegation=True, # 允许在需要时求助
  llm=local_llm
)
```

### 第2步：分配具体的Task

为我们定义好的Agent分配具体的、一次性的任务。

```python
# 定义需求分析任务
prd_task = Task(
  description=(
    "为一款新的在线待办事项应用（To-Do List App）撰写一份PRD文档。"
    "需要包含核心用户故事、主要功能列表（创建、编辑、删除、标记完成）"
    "以及基本的非功能性需求（如性能、安全）。"
  ),
  expected_output='一份完整的Markdown格式的PRD文档。',
  agent=pm # 将任务分配给产品经理
)

# 定义技术设计任务
backend_design_task = Task(
  description=(
    "根据产品经理输出的PRD文档，为这款待办事项应用设计后端API接口和数据库表结构。"
  ),
  expected_output='一个包含API端点定义和SQL表结构设计的Markdown文档。',
  agent=backend_developer, # 将任务分配给后端工程师
  context=[prd_task], # 核心！明确指定该任务的上下文来自于prd_task
)
```

### 第3步：组建Crew并启动

将你的Agent和Task组建成一个“项目组”，并设定协作流程。

```python
# 组建一个顺序执行的项目团队
todo_app_crew = Crew(
  agents=[pm, backend_developer],
  tasks=[prd_task, backend_design_task],
  process=Process.sequential, # 任务按顺序执行
  verbose=2,
)

# 启动任务
result = todo_app_crew.kickoff()

print("######################")
print("CrewAI任务执行结果:")
print(result)

```

## 从“能跑”到“好用”：三大核心挑战的解决方案

上面的代码只是“骨架”，它能跑，但离生产还有距离。在我们最近的深度探讨中，我们共同识别出了将这副骨架变为强大战力的三大核心挑战，并找到了具体的解决方案。

### 1. 上下文管道 (Context Pipelining)：解决信息精准传递

**挑战：** `prd_task`的输出（一篇几十上百行的PRD文档）如何精准地成为`backend_design_task`的输入？如果只是简单地将上一步结果塞入下一步的Prompt，很容易造成上下文污染和信息丢失。

**解决方案：** 正如我们在新代码中加入的`context=[prd_task]`。这是CrewAI的“上下文管道”机制。它并非简单粗暴地拼接Prompt，而是将`prd_task`的**纯净输出结果**，作为一个结构化的上下文，精准地注入到`backend_design_task`的执行环境中。这保证了信息流的干净、无损，是构建可靠工作流的基石。

### 2. 自定义工具 (Custom Tools) 与委托：解决任务粒度与复杂性

**挑战：** 如果一个任务非常复杂，比如“请完成整个后端的开发”，`Task`定义得太粗，Agent容易“自由发挥”导致不可控；定义得太细，又失去了AI的创造性。

**解决方案：** 引入“自定义工具”，这完美呼应了我们“高速公路+特种部队”的设想。我们可以将一个极其复杂的、需要深度代码理解的任务，封装成一个强大的“特种部队”工具，然后授权给CrewAI里的某个Agent来调用。

例如，我们可以封装一个`ClaudeCodeExecutionTool`：

```python
import subprocess
from crewai_tools import BaseTool

class ClaudeCodeExecutionTool(BaseTool):
    name: str = "Claude Code 专家执行器"
    description: str = (
        "当你需要完成一个非常复杂的、高阶的开发或修复任务时，"
        "调用此工具。它会启动一个独立的、具备深度代码库理解能力的AI专家（如Claude Code）"
        "来执行这个任务，并返回最终的结果。"
    )

    def _run(self, task_description: str) -> str:
        # 这是一个示例，实际中会调用Claude Code的CLI或API
        command = f'claude-code-cli --task "{task_description}"'
        try:
            result = subprocess.check_output(
                command, 
                shell=True, 
                text=True, 
                stderr=subprocess.STDOUT
            )
            return f"独立的Claude Code专家任务成功完成，结果如下：\n{result}"
        except subprocess.CalledProcessError as e:
            return f"独立的Claude Code专家任务执行失败，错误信息：\n{e.output}"

# 然后在定义Agent时，将这个工具交给他
# backend_developer = Agent(
#   ...,
#   tools=[ClaudeCodeExecutionTool()]
# )
```
通过这种方式，CrewAI负责流程的“高速公路”，而复杂的执行细节则被“委托”给了最专业的工具。

### 3. 人机回环 (Human in the Loop)：解决动态反馈与调试

**挑战：** 一次性输出的PRD或代码往往不完美，我们需要一个机制来反复地“评审-反馈-修改”，直到我们满意为止。

**解决方案：** 将CrewAI的执行过程，置于一个“人机回环”之中。这不需要CrewAI内部支持，只需要在外部调用脚本中实现即可。

例如，一个多轮PRD评审的伪代码：

```python
prd_approved = False
user_feedback = "这是我的初始需求：做一个在线待办事项应用。"
last_prd_draft = "无"

while not prd_approved:
    prd_task = Task(
      description=f"""
      根据用户的最新反馈，优化或创建PRD文档。
      上一版草稿是：{last_prd_draft}
      用户的最新反馈是：'{user_feedback}'
      """,
      expected_output="一份更新后的、完整的Markdown格式的PRD文档。",
      agent=pm
    )

    prd_crew = Crew(agents=[pm], tasks=[prd_task])
    current_prd_draft = prd_crew.kickoff()
    
    print("----------- 新版PRD草稿 -----------")
    print(current_prd_draft)
    print("---------------------------------")
    
    user_feedback = input("请审阅新版PRD。如果满意请输入'ok'，否则请输入您的修改意见：")

    if user_feedback.lower() == 'ok':
        prd_approved = True
        print("PRD已批准，进入下一阶段！")
    else:
        last_prd_draft = current_prd_draft # 保存当前版本，用于下一轮迭代
```

这个简单的`while`循环，就构建了一个强大的、允许无限次反馈和迭代的人机协作系统。

## 进阶用法：并行处理与层级管理 (Hierarchical Process)

我们之前的例子是`Process.sequential`顺序执行。但真正的团队开发，往往是并行的。比如UI/UX设计完成后，Web、iOS、Android客户端的开发可以同时进行。CrewAI通过`Process.hierarchical`（层级模式）来支持这一点。

在层级模式下，你需要指定一个“管理者Agent”，它负责将任务分解，并监督其他Agent并行工作。

```python
# 伪代码示例

# 1. 定义各个客户端的开发Agent
web_developer = Agent(role='Web前端工程师', ...)
ios_developer = Agent(role='iOS工程师', ...)
android_developer = Agent(role='安卓工程师', ...)

# 2. 定义并行开发任务
web_task = Task(description='根据UI设计稿和PRD，开发Web客户端', agent=web_developer)
ios_task = Task(description='根据UI设计稿和PRD，开发iOS客户端', agent=ios_developer)
android_task = Task(description='根据UI设计稿和PRD，开发安卓客户端', agent=android_developer)

# 3. 定义一个“技术经理”或“项目经理”作为管理者
manager_agent = Agent(
    role='技术经理',
    goal='协调并管理所有客户端的并行开发，确保最终交付物的一致性和高质量',
    ...,
    allow_delegation=True # 必须允许管理者授权
)

# 4. 组建层级团队
parallel_crew = Crew(
  agents=[web_developer, ios_developer, android_developer, manager_agent],
  tasks=[web_task, ios_task, android_task],
  process=Process.hierarchical,
  manager_llm=local_llm # 为管理者指定一个LLM
)

# 启动并行任务
parallel_result = parallel_crew.kickoff()
```

通过这种模式，我们就从一条“流水线”进化成了一个拥有“多个并行的事业部”的组织。

## 总结：从“总设计师”到“AI公司创始人”

通过引入上下文管道、自定义工具、人机回环以及并行处理，CrewAI让我们彻底超越了“手工作坊”的模式。

我们的角色，也从繁琐的“人肉导演”，或者仅仅是设计工作流的“总设计师”，进一步升华为了一个**“AI公司创始人”**。

我们的核心工作变成了：
1.  **设定公司战略 (Why)：** 决定我们要解决什么问题，如《AI Agent的“规则”之困与架构破局》一文所探讨的。
2.  **构建组织架构 (Who & How)：** 定义`Agents`, `Tasks`, `Process`，搭建我们的AI公司。
3.  **打造核心工具 (What)：** 封装`Custom Tools`，为我们的AI员工提供最强大的生产力工具。
4.  **把握产品方向 (Iterate)：** 通过“人机回环”，确保公司的最终产出符合我们的愿景。

CrewAI为我们提供了一套完整的、可无限扩展的框架，让我们能真正地**设计和经营**一个属于自己的AI团队。这，才是AI协作的未来。

大家觉得，当我们能用代码像经营一家公司一样经营我们的AI团队时，还有哪些过去不敢想的事情，现在变得可能了？欢迎在评论区分享你的畅想！

---
William
分享连接你我，AI点燃心火。 
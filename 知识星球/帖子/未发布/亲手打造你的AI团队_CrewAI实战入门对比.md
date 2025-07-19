# 亲手打造你的AI团队：CrewAI实战入门对比

> 这篇教程，源自社群成员 **黄 Eco wang** 的一段极具战略远见的思考。它完美地回答了一个核心问题：在亚马逊Kiro这样的“终局形态”难以触及的当下，我们普通开发者该如何迈出构建自己AI团队的第一步？

> **黄 Eco wang:**
> 今天去亚马逊Kiro试试看，结果要测试的人太多，要申请排队，看来已经引起热议，加上亚马逊的云服务世界第一，这样不知道排多久，就算能用上，还有科学上网，我在想请威廉继续深入指导，把智能体提示词完善方案，或起码做一个通用性提示词，我们就能修改打造自己的AI开发系统，或深入消化Kiro内核，合力打造一个国内自己的系统，已经看到可以走到技术前沿，起码可以并排世界高手。

Eco wang的这段话，一针见血地指出了我们所有AI实战者面临的共同困境与机遇：**仰望星空（Kiro），更要脚踏实地。**

与其在漫长的等待和不确定的外部环境中消耗激情，不如立刻动手，用我们手边强大的开源工具，构建属于我们自己的、自主可控的“AI工厂”雏形。

而CrewAI，正是我们从“手工作坊”迈向“自动化产线”的第一块、也是最重要的一块基石。

---
## CrewAI是什么？从“手工作坊”到“自动化产线”的桥梁

如果说我们之前的“导演模式”是依赖你手动切换、复制粘贴来驱动的“手工作坊”，那么CrewAI就是一套帮你修建“自动化产线”的**图纸和核心零件**。

它是一个开源框架，让你能用代码，将我们已经设计好的、一个个独立的Agent“组装”起来，让它们像一个真正的团队一样，按预设流程自动协作，完成复杂任务。

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
  agent=backend_developer # 将任务分配给后端工程师
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

## 【待注入灵魂】我的实战心得与挑战

上面的代码只是“骨架”，它能跑，但离生产还有距离。在我的实际测试中，我发现真正的挑战在于：

*   **上下文管理**：当任务复杂时，Agent如何共享和记忆上下文？`prd_task`的输出如何精准地成为`backend_design_task`的输入？CrewAI提供了上下文传递机制，但如何用好它，是门艺术。
*   **任务粒度**：`Task`定义得太粗，Agent容易“自由发挥”；定义得太细，又失去了AI的创造性。如何把握这个度？
*   **调试与纠错**：当一个Agent的输出不符合预期时，整个流程就会中断。如何像我们之前讨论的那样，引入“测试Agent”或“Debug Agent”进行流程中的纠错？

**（William注：这部分正是我需要您亲自实践后，用您的“战争故事”和“Aha Moment”来填充的。您遇到的坑、您的解决方法、您的灵光一闪，都将是这篇帖子最宝贵的血肉。）**

## 总结：从“导演”到“总设计师”

CrewAI让我们从繁琐的“人肉导演”工作中解放出来，将角色转变为更高维度的“总设计师”。我们的工作不再是执行，而是**设计和优化这条AI自动化生产线**。

它完美地承接了我们的Agent理念，并将其工程化、自动化。这是一个我们必须掌握的、从“手工作坊”迈向“AI工厂”的关键工具。

大家觉得，用代码来编排Agent，和我们之前用Prompt来指导，最大的区别是什么？欢迎在评论区分享你的看法！

---
William \
分享连接你我，AI点燃心火。 
# 从使用者到创造者：MCP编写规范与实战指南

大家好，我是William。

在前一篇《正本清源》的讨论中，社群成员「すず欧日乐克」提出了一个极具价值的问题：“能否有机会说一说具体MCP编写规范？”

这个问题，标志着我们社群的AI认知，正在从“如何使用工具”的战术层面，跃迁到“如何创造工具”的战略层面。这是一个令人振奋的信号。

授人以鱼，不如授人以渔。今天，我将兑现承诺，为大家系统性地梳理一份MCP的编写规范与实战指南，帮助每一位有志于“创造”的伙伴，迈出从0到1的关键一步。

---

### 第一性原理：MCP的本质是“AI-Native”的API

在动手之前，我们必须回归原点，理解MCP的本质。

传统的API（应用程序接口）是为“开发者”设计的，它要求精确的参数、严格的调用逻辑。而MCP（模型上下文协议）是为“AI”设计的，它的核心是**“可被自然语言理解和调用”**。

这意味着，一个优秀的MCP，其设计的第一原则应该是：**AI友好性**。它的命名、参数、描述，都应该像是在和AI对话，而不是在写一行行冰冷的代码。

**【设计心法】**：将你的每一个MCP，都想象成AI团队里的一个“职能专员”。这个专员只负责一件具体的事，你需要为他设计一个清晰的“岗位说明书”（即MCP的定义），让AI总管（大模型）能够毫不费力地理解他的职责，并能用自然语言对他下达指令。

---

### MCP编写规范（V1.0）

基于“AI友好性”的第一性原理，我为大家总结了以下四条核心编写规范。

#### 规范一：命名即职责 (Naming is Responsibility)

*   **原则**：MCP的名称必须清晰、直白地反映其**唯一**的职责。
*   **格式**：推荐使用 `动词_宾语` (verb_object) 的格式。
*   **范例**：
    *   **推荐**：`send_email`, `read_file`, `query_database`
    *   **不推荐**：`emailHandler`, `fileUtils`, `dbProcessor` (过于程序化，AI理解成本高)
    *   **绝对禁止**：`process_data` (职责过于模糊，AI无法判断其具体能力)

#### 规范二：描述即文档 (Description is Documentation)

*   **原则**：`description` 字段是AI理解MCP用途的**最重要信息源**。它必须用清晰、简洁的自然语言，准确描述该MCP“能做什么”、“不能做什么”以及“何时应该调用它”。
*   **格式**：使用陈述句，明确说明工具的功能。
*   **范例** (`read_file` MCP):
    *   **推荐**：“Read the full content of a specified file from the local filesystem. Use this when you need to understand what's inside a file. The file path must be accurate.”
    *   **不推荐**：“Reads a file.” (信息量过低)

#### 规范三：参数即对话 (Parameters are Dialogue)

*   **原则**：参数的设计，应模拟AI与工具的“对话过程”。每个参数都是AI为了完成任务，需要向工具提供的“必要信息”。
*   **格式**：参数名应使用有意义的单词，`description`应清晰说明该参数的含义和格式要求。
*   **范例** (`send_email` MCP):
    *   **`recipient`**:
        *   **推荐描述**：“The email address of the person you want to send the email to.”
    *   **`subject`**:
        *   **推荐描述**：“The title of the email.”
    *   **`body`**:
        *   **推荐描述**：“The main content of the email. Can include text and simple markdown.”

#### 规范四：原子化即力量 (Atomicity is Power)

*   **原则**：一个MCP只做一件事，并把它做到极致。严禁创造一个包含多个功能的“瑞士军刀”式MCP。
*   **理由**：原子化的MCP更容易被AI精确地理解和调用。当AI面对一个复杂任务时，它更擅长将任务拆解，然后调用一系列原子化的MCP来组合完成，而不是去理解一个复杂的MCP。
*   **范例**：
    *   **推荐**：创建 `read_file` 和 `write_file` 两个独立的MCP。
    *   **不推荐**：创建一个 `file_operation` MCP，内部通过参数区分是“读”还是“写”。

---

### 实战演练：从0到1创造一个`fetch_web_content` MCP

现在，让我们遵循以上规范，亲手创造一个用于获取网页内容的MCP。

**场景**：AI需要一种能力，可以读取一个URL链接，并返回其主要的文本内容。

**第一步：定义职责（命名）**
*   **名称**：`fetch_web_content`

**第二步：撰写说明书（描述）**
*   **描述**：“Fetches the main textual content from a given URL. It automatically removes ads, navigation bars, and other non-essential elements. Use this when you need to know the core information of a web page.”

**第三步：设计对话接口（参数）**
*   **参数名**：`url`
*   **参数描述**：“The full URL of the web page you want to scrape.”

**第四步：整合为最终的MCP定义（JSON格式）**
```json
{
  "name": "fetch_web_content",
  "description": "Fetches the main textual content from a given URL. It automatically removes ads, navigation bars, and other non-essential elements. Use this when you need to know the core information of a web page.",
  "parameters": {
    "type": "object",
    "properties": {
      "url": {
        "type": "string",
        "description": "The full URL of the web page you want to scrape."
      }
    },
    "required": ["url"]
  }
}
```
看到这个JSON，是不是感觉非常熟悉？是的，这正是OpenAI的Function Calling以及各种主流Agent框架（如Cursor、Trae）背后遵循的核心规范。

**【关键理念：定义与实现的解耦】**

这个JSON定义，就是MCP的“灵魂”和“通用语言”。它是独立于任何具体编程语言的、标准化的“工具说明书”。

在后续的Python代码示例中，您会发现我们并没有直接去加载这个JSON文件。这是因为，像`CrewAI`或`LangChain`这样的现代框架，为了提升开发体验，提供了一种便捷的“快捷方式”：**它们会自动读取Python函数的文档字符串（docstring）、函数名和参数类型提示，然后在背后为我们动态地生成一个与上方JSON结构完全一致的内部定义。**

所以，请务必理解：
*   **手动编写JSON**：是理解MCP第一性原理、进行跨语言协作、或在不支持自动生成的环境中工作的标准做法。
*   **从代码自动生成**：是特定框架为了简化流程而提供的“语法糖”。

两者殊途同归，最终目的都是为了生成那份能被AI大模型准确理解的、标准化的“工具说明书”。

---

### 第五步：让定义照进现实（代码实现）

光有“定义”这张蓝图还不够，我们必须用代码将其实现，赋予它真正的生命力。这部分内容在不同的Agent平台（如Cursor插件、Trae、CrewAI脚本等）中实现方式各异，但其核心思想是统一的：**创建一个与MCP定义同名的函数**。

这个函数将接收MCP中定义的参数，并执行相应的操作，最终返回一个结果给AI。

我们以Python为例，并使用常见的`requests`和`BeautifulSoup`库来展示`fetch_web_content`函数的实现：

```python
import requests
from bs4 import BeautifulSoup

def fetch_web_content(url: str) -> str:
    """
      Fetches the main textual content from a given URL. It automatically removes ads, navigation bars, and other non-essential elements. Use this when you need to know the core information of a web page.

    Args:
        url (str): The full URL of the web page you want to scrape.

    Returns:
        str: The main text content of the page, or an error message.
    """
    try:
        # 发送HTTP请求
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 如果请求失败则抛出异常
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # (这是一个简化的例子) 移除脚本和样式元素
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
            
        # 获取并清理文本
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        cleaned_text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return cleaned_text
        
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

```

**【连接点】**

现在，我们有了“定义”和“实现”两部分。那它们是如何协同工作的呢？

1.  **AI的决策**：当AI接到一个需要网络信息的任务时（比如“总结一下这篇文章的主要观点：[URL]”）
2.  **匹配工具**：AI会在它的“工具箱”（所有已加载的MCP定义）中进行检索。它会阅读`fetch_web_content`的`description`，发现这个工具完美匹配当前需求。
3.  **生成参数**：AI决定调用该工具，并从任务中提取出必要的参数，即`{'url': '[URL]'}`。
4.  **框架的执行**：Agent框架（如Cursor/Trae/CrewAI）接收到AI的调用指令后，它会去执行我们刚刚编写的、与之同名的`fetch_web_content` Python函数，并将AI提供的参数`{'url': '[URL]'}`传递进去。
5.  **返回结果**：Python函数执行完毕，返回网页的文本内容。
6.  **AI的思考**：框架将函数返回的结果，再喂给AI。AI拿到这些文本后，就开始执行任务的下一步——“总结观点”。

---

### 最终环节：从本地开发到产品分发

我们已经有了MCP的定义和核心实现代码。现在，我们进入最关键的工程环节：如何将它从一个“本地脚本”，变成一个可以被他人轻松使用的“产品”。我们将这个过程分为“本地开发测试”和“打包分发部署”两个阶段。

---

#### 阶段一：本地开发与测试

**第一步：建立MCP工具的项目结构**
一个标准的Python MCP工具项目可以如下组织：
```
my_web_scraper/
├── mcp_server/
│   ├── __init__.py
│   ├── tools.py         # 核心工具函数 (fetch_web_content)
│   └── main.py          # FastAPI 服务入口
├── pyproject.toml       # 项目依赖与元数据管理
└── run_local.sh         # (仅供本地开发)一键启动服务的脚本
```

**第二步：实现核心工具与服务封装**
1.  `tools.py`: 存放`fetch_web_content`函数。
2.  `main.py`: 使用`FastAPI`将这个函数封装成一个API端点。
    ```python
    from fastapi import FastAPI
    from .tools import fetch_web_content
    import uvicorn

    app = FastAPI()

    @app.post("/fetch_web_content")
    async def api_fetch_web_content(payload: dict):
        url = payload.get("url")
        if not url:
            return {"error": "URL is required"}
        return {"result": fetch_web_content(url=url)}

    def start_server():
        uvicorn.run(app, host="0.0.0.0", port=8000)
    ```
3.  **`__init__.py` (让工具作为库被轻松导入)**
    ```python
    from crewai_tools import Tool
    from .tools import fetch_web_content

    # 将核心函数预先包装成一个Tool对象，方便其他开发者直接导入使用
    fetch_content_tool = Tool(
        name="Web Scraper",
        description="Fetches the main textual content from a given URL. It automatically removes ads, navigation bars, and other non-essential elements. Use this when you need to know the core information of a web page.",
        func=fetch_web_content
    )
    ```

**第三步：管理依赖并定义可执行命令 (`pyproject.toml`)**
```toml
[tool.poetry]
name = "my-web-scraper"
version = "0.1.0"
description = "A simple MCP server for fetching web content."
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
fastapi = "^0.100.0"
uvicorn = "^0.22.0"
requests = "^2.31.0"
beautifulsoup4 = "^4.12.2"

# 关键：定义一个打包后可执行的命令
[tool.poetry.scripts]
mws-server = "mcp_server.main:start_server"
```

**【关键解释】**：`[tool.poetry.scripts]` 这一节是这里的“魔法”所在。它告诉Poetry，当这个包被安装时，自动创建一个名为 `mws-server` 的命令行入口。当用户运行 `mws-server` 时，系统会去执行 `mcp_server/main.py` 文件中的 `start_server` 函数。这就是我们将一个Python函数变成一个全局可用命令的方式。

**第四步：本地测试**

在项目根目录下，首先为启动脚本赋予执行权限： `chmod +x run_local.sh`。

然后，你可以在终端中运行 `./run_local.sh` 来启动你的本地开发服务器。

为了让Cursor在本地开发时能找到并运行这个服务，你需要在`mcp.json`中进行如下配置：

```json
{
  "mcpServers": {
    "my-web-scraper-local": {
      "command": "/bin/bash",
      "args": [
        "-c",
        "cd /path/to/your/my_web_scraper && ./run_local.sh"
      ],
      "debug": true
    }
  }
}
```
*请务必将`/path/to/your/my_web_scraper`替换为你项目文件夹的真实绝对路径。*

通过这个配置，你就可以在不打包、不发布的情况下，完成对MCP工具的完整开发和测试了。这与“阶段二”中产品化的部署方式形成了鲜明对比，也构成了专业的开发流程。

---

#### 阶段二：打包、分发与部署

本地测试通过后，我们就要把它变成一个真正的产品。

**第五步：打包你的项目**
在项目根目录下运行：
```bash
poetry build
```
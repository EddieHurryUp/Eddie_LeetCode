# Eddie_LeetCode

个人 LeetCode 刷题仓库（Python），用于面试准备与题解复盘。

## 仓库结构

- `*.py`：按题号命名的题目代码
- `测试开发实习面试-LeetCode10题清单.md`：面试冲刺清单

## 题目索引

| 题号 | 题目 | 文件 |
| --- | --- | --- |
| 1 | 两数之和 | `1.两数之和.py` |
| 5 | 最长回文子串 | `5.最长回文子串.py` |
| 49 | 字母异位词分组 | `49.字母异位词分组.py` |

## 刷题规范

- 每题包含：核心思路、复杂度、易错点（可写在代码末尾注释）
- 提交信息建议：`feat(leetcode): <题号> <题名>`
- 常用 Git 流程：

```bash
git add .
git commit -m "feat(leetcode): 1 two sum"
git push
```

## 近期目标

- 完成测试开发实习面试 10 题清单第一轮
- 每题至少补 3 类测试用例：正常、边界、极端

## Docker 学习与实战（基于本仓库）

### 1) Docker 是什么

Docker 可以把你的代码和运行环境一起打包成一个镜像（image），然后在任意机器上用容器（container）运行。  
它的核心价值是：**环境一致、迁移方便、启动快**。

你可以先记住 3 个概念：

- `镜像 Image`：像一个只读模板（包含 Python、代码、依赖）
- `容器 Container`：镜像启动后的运行实例（可启动、停止、删除）
- `Dockerfile`：定义“如何构建镜像”的脚本

### 2) 本仓库已提供的 Docker 文件

- `Dockerfile`：使用 `python:3.12-slim`，默认运行 `1.两数之和.py`
- `.dockerignore`：构建时忽略 `.git`、缓存等无关文件

### 3) 一次完整流程（建议直接实操）

在仓库根目录执行：

```bash
# 1. 构建镜像（镜像名自定义）
docker build -t eddie-leetcode:latest .

# 2. 运行默认命令（1.两数之和）
docker run --rm eddie-leetcode:latest
```

你会看到类似输出：

```text
[0, 1]
```

### 4) 运行其他题目文件

容器运行时可以覆盖默认命令：

```bash
docker run --rm eddie-leetcode:latest python "20.有效的括号.py"
docker run --rm eddie-leetcode:latest python "206.反转链表.py"
```

### 5) 挂载本地代码（边改边跑）

刷题时更推荐把本地仓库挂载进容器，这样你改完代码不用重新 build：

```bash
docker run --rm -it \
  -v "$(pwd)":/app \
  -w /app \
  python:3.12-slim \
  python "1.两数之和.py"
```

说明：

- `-v "$(pwd)":/app`：把当前目录挂载到容器 `/app`
- `-w /app`：进入工作目录 `/app`
- 使用官方 Python 镜像直接执行脚本

### 6) 常用排错命令

```bash
# 查看本机镜像
docker images

# 查看运行中的容器
docker ps

# 查看所有容器（包括已退出）
docker ps -a

# 删除镜像（如果需要重建）
docker rmi eddie-leetcode:latest
```

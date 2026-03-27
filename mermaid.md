# Mermaid 功能展示手册

这个文件用于快速体验 Mermaid 在 Markdown 中可绘制的常见图表。  
在 VS Code 中打开本文件后，使用 Markdown 预览即可看到效果。

## 1) Flowchart（流程图）
适合：算法流程、条件分支、系统处理流程。

```mermaid
flowchart TD
    A([Start]) --> B[读取输入]
    B --> C{输入是否合法?}
    C -- 是 --> D[执行业务逻辑]
    C -- 否 --> E[返回错误]
    D --> F[输出结果]
    E --> F
    F --> G([End])
```

## 2) Sequence Diagram（时序图）
适合：接口调用链、服务间交互、消息流程。

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant FE as Frontend
    participant API as Backend API
    participant DB as Database

    U->>FE: 点击提交
    FE->>API: POST /submit
    API->>DB: 写入记录
    DB-->>API: 返回成功
    API-->>FE: 200 OK
    FE-->>U: 展示成功提示
```

## 3) Class Diagram（类图）
适合：面向对象建模、代码结构梳理。

```mermaid
classDiagram
    class ListNode {
        +int val
        +ListNode next
    }

    class Solution {
        +reverseList(head) ListNode
        +twoSum(nums, target) List[int]
    }

    Solution ..> ListNode : uses
```

## 4) State Diagram（状态图）
适合：状态机、任务生命周期、订单状态流转。

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Reviewing : submit
    Reviewing --> Approved : approve
    Reviewing --> Rejected : reject
    Rejected --> Draft : modify
    Approved --> [*]
```




## 5) ER Diagram（实体关系图）
适合：数据库表关系、字段结构说明。

```mermaid
erDiagram
    USER ||--o{ SUBMISSION : creates
    PROBLEM ||--o{ SUBMISSION : receives

    USER {
        int id PK
        string name
        string email
    }

    PROBLEM {
        int id PK
        string title
        string difficulty
    }

    SUBMISSION {
        int id PK
        int user_id FK
        int problem_id FK
        string language
        string status
    }
```

## 6) Gantt（甘特图）
适合：学习计划、项目排期、迭代节奏。

```mermaid
gantt
    title LeetCode 冲刺计划
    dateFormat  YYYY-MM-DD
    section 第一阶段
    数组与哈希       :done,    t1, 2026-03-15, 3d
    栈与队列         :active,  t2, after t1, 3d
    链表与双指针     :         t3, after t2, 4d
    section 第二阶段
    树与递归         :         t4, after t3, 5d
    动态规划         :         t5, after t4, 6d
```

## 7) Pie（饼图）
适合：占比展示、题型分布。

```mermaid
pie showData
    title 刷题题型占比
    "数组" : 35
    "链表" : 20
    "栈" : 15
    "树" : 20
    "动态规划" : 10
```

## 8) Journey（用户旅程图）
适合：用户体验路径、学习过程可视化。

```mermaid
journey
    title LeetCode 每日学习旅程
    section 早上
      阅读题目与思考: 1: 学习者
      写出初版解法: 4: 学习者
    section 下午
      调试与优化复杂度: 3: 学习者
      补充边界测试: 4: 学习者
    section 晚上
      复盘总结与记忆卡片: 5: 学习者
```

## 9) Git Graph（Git 提交图）
适合：分支策略、提交关系说明。

```mermaid
gitGraph
    commit id: "init"
    branch feature/docker
    checkout feature/docker
    commit id: "add Dockerfile"
    commit id: "update README"
    checkout main
    merge feature/docker
    commit id: "release v1"
```

## 10) Mindmap（思维导图）
适合：知识体系整理、面试知识图谱。

```mermaid
mindmap
  root((LeetCode))
    数据结构
      数组
      链表
      栈
      树
    算法思想
      双指针
      二分
      贪心
      动态规划
    工程实践
      单元测试
      复杂度分析
      复盘总结
```

## 11) Timeline（时间线）
适合：里程碑展示、学习进度记录。

```mermaid
timeline
    title 面试准备时间线
    2026-03 : 完成数组与哈希专题
    2026-04 : 完成链表与树专题
    2026-05 : 完成动态规划与系统复盘
```

## 12) Requirement Diagram（需求图）
适合：需求与实现映射、测试覆盖梳理。

```mermaid
requirementDiagram
    requirement req_perf {
      id: REQ_1
      text: "接口响应时间小于 200ms"
      risk: Medium
      verifymethod: Test
    }

    requirement req_correct {
      id: REQ_2
      text: "算法结果正确率 100%"
      risk: High
      verifymethod: Test
    }

    element tc_perf {
      type: "TestCase"
      docref: "TC_1: 压测 1000 次请求"
    }

    element tc_case {
      type: "TestCase"
      docref: "TC_2: 边界/极端用例集"
    }

    tc_perf - verifies -> req_perf
    tc_case - verifies -> req_correct
```

## 13) XY Chart（实验性）
适合：趋势、对比分析（不同算法耗时）。

```mermaid
xychart-beta
    title "算法耗时对比"
    x-axis [BruteForce, HashMap, TwoPointers]
    y-axis "ms" 0 --> 50
    bar [42, 9, 15]
```

## 14) Quadrant Chart（实验性）
适合：策略评估、方案对比。

```mermaid
---
id: cd7d300d-2660-4091-8c08-96f3060011f4
---
quadrantChart
    title "题目训练策略"
    x-axis "低难度" --> "高难度"
    y-axis "低收益" --> "高收益"
    quadrant-1 "挑战区"
    quadrant-2 "高价值区"
    quadrant-3 "低优先区"
    quadrant-4 "刷熟练区"
    "简单题刷熟": [0.3, 0.3]
    "中等题复盘": [0.5, 0.7]
    "难题突破": [0.8, 0.8]
    "偏题练习": [0.7, 0.2]
```

## 快速说明
- 如果某些“实验性图表”在你的插件版本不显示，先升级 Mermaid 插件或切换为前面的基础图表类型。
- 最常用、兼容最好的类型：`flowchart`、`sequenceDiagram`、`classDiagram`、`stateDiagram-v2`、`erDiagram`、`gantt`、`pie`。

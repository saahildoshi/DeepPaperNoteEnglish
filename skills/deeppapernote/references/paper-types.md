# Paper Types

Every note keeps the same 12 top-level sections from `NOTE_REQUIRED_SECTIONS`.
Paper type only changes the typed semantics of shared sections and the recommended `###` subsections used in `note_plan.section_plan`.

Use `contracts_by_paper_type[note_plan.paper_type]` as the canonical structured source:
- `section_semantics`: how each fixed top-level section should be interpreted for this paper type.
- `recommended_subsections`: paper-type-specific `###` candidates for technical or analytical sections.
- `boundary_questions`: paper-type-specific questions that should shape `central_claims`, `claim_boundaries`, `negative_or_limiting_results`, `mechanism_result_map`, `comparative_positioning`, and `followup_questions`.

## `AI_method`

section_semantics:
- Research Question: 方法要解决的具体技术问题和现有方法短板。
- Data & Task Definition: 数据集、输入输出、评测任务和实验设置。
- Method Mainline: 模型、算法、训练或推理机制。
- Key Results: 主结果、强基线、消融和关键数字。
- In-depth Analysis: 方法为什么有效、何处脆弱、复现和扩展代价。

recommended_subsections:
- Method Mainline: `Mechanism Flow`, `模型结构`, `训练目标`, `推理与采样链路`, `关键实现细节`
- Key Results: `主结果与强基线`, `消融到底说明了什么`, `失败或不稳定设置`
- In-depth Analysis: `为什么有效`, `复杂度与扩展性`, `复现注意点`

boundary_questions:
- 核心机制的收益由哪个实验或消融支撑，而不是只由主结果暗示？
- 哪些比较只能证明在当前数据、基线、算力或协议下有效，不能外推到通用场景？
- 论文是否给出失败、退化、不稳定或成本上升的证据；如果没有，结论边界是什么？

## `benchmark_or_dataset`

section_semantics:
- Research Question: 这个 benchmark/dataset 想补足的评测或数据缺口。
- Data & Task Definition: 数据来源、任务拆分、标签/题目定义、样本范围。
- Method Mainline: 数据构建、筛选、标注和评测协议，不写成模型 pipeline。
- Key Results: 基线表现、难度分布、覆盖范围和偏差。
- In-depth Analysis: 它真正测到了什么，以及不能代表什么。

recommended_subsections:
- Data & Task Definition: `数据来源`, `任务拆分`, `标注/筛选协议`
- Method Mainline: `构建流程`, `评测协议`, `Baseline 设置`
- Key Results: `基线表现`, `难度分布`, `覆盖与偏差`
- In-depth Analysis: `benchmark 真正测到了什么`, `适用边界`

boundary_questions:
- 这个 benchmark/dataset 实际测量的构念是什么，哪些能力只是间接近似？
- 任务、标签、采样、过滤或评测协议会引入哪些覆盖缺口或偏差？
- 基线结果证明了评测集有区分度，还是只证明某类模型适应该协议？
- 样本时长、语料长度、人口统计、类别分布、数据可访问性或隐私限制如何影响复现和外推？

## `clinical_or_psychology_empirical`

section_semantics:
- Research Question: 临床、心理学或行为科学中的Research Question、假设或变量关系。
- Data & Task Definition: 样本来源、纳排标准、变量/量表、测量方式。
- Method Mainline: 研究设计、分组、测量流程和统计分析路径。
- Key Results: 主要效应、相关性、组间差异、不确定性或显著性。
- In-depth Analysis: 结果解释、因果边界、临床/心理学意义和外推限制。

recommended_subsections:
- Data & Task Definition: `样本与纳排标准`, `变量与量表`, `测量流程`
- Method Mainline: `研究设计`, `分析模型`, `主要比较`
- Key Results: `主要效应`, `不确定性与显著性`, `临床或心理学解释`
- In-depth Analysis: `因果解释边界`, `外推限制`

boundary_questions:
- 样本来源、纳排标准、测量工具和标注流程如何限制外推？
- 结果支持相关、预测、组间差异还是因果解释；不要越过论文设计能证明的范围。
- 临床或心理学意义是否依赖未观测混杂、量表阈值、文本/语音缺失或场景约束？
- 样本构成、数据缺失、隐私限制或材料不可公开会怎样限制复现与再分析？

## `humanities_or_social_science`

section_semantics:
- Research Question: Authors要解释的社会、文化、历史、制度或理论问题。
- Data & Task Definition: 材料、案例、文本、访谈、档案或语料范围，不写成 ML task。
- Method Mainline: 理论框架、概念区分和论证路径。
- Key Results: 核心解释性发现、概念贡献或对既有观点的修正。
- In-depth Analysis: 论证强度、材料边界、解释替代性和可迁移性。

recommended_subsections:
- Data & Task Definition: `材料范围`, `选择标准`, `案例或语料边界`
- Method Mainline: `理论框架`, `概念区分`, `论证路径`
- Key Results: `核心解释性发现`, `概念贡献`
- In-depth Analysis: `论证强度`, `替代解释`, `材料边界`

boundary_questions:
- Authors的解释依赖哪些材料、案例或理论前提？
- 是否存在同样能解释材料的替代解释，论文如何排除或没有排除？
- 哪些结论是概念贡献或规范性判断，而不是可直接当作经验事实？

## `survey_or_review`

section_semantics:
- Research Question: 综述试图整理的领域问题、争议或知识缺口。
- Data & Task Definition: 纳入文献范围、检索/筛选标准和综述对象。
- Method Mainline: 分类体系、综述组织方式和证据综合逻辑，不写成单篇方法架构。
- Key Results: 领域共识、分歧、趋势、代表性方向和开放问题。
- In-depth Analysis: 综述覆盖的盲区、分类体系的解释力和未来研究机会。

recommended_subsections:
- Data & Task Definition: `综述范围`, `纳入/排除标准`, `文献覆盖`
- Method Mainline: `分类体系`, `方法谱系`, `证据组织方式`
- Key Results: `代表性方向`, `共识与分歧`, `开放问题`
- In-depth Analysis: `分类体系的Limitations`, `未覆盖区域`, `后续研究机会`

boundary_questions:
- 检索范围、纳入排除标准或分类轴会遗漏哪些研究路线？
- 综述给出的是领域共识、Authors分类，还是尚未解决的分歧？
- 哪些趋势结论来自覆盖范围内的文献分布，不能直接当作技术成熟度判断？

## Selection Rule

Choose one primary `note_plan.paper_type` from the synthesis bundle's allowed values first.
Then keep the fixed top-level sections and use that paper type's `section_semantics` plus `recommended_subsections` to write `note_plan.section_plan`.

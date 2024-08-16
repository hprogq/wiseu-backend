# WiseU

## About WiseU
WiseU is a **Wise Campus Life Assistant** For **University Students**.

This is a developing group project in 2024 CNTDxDLUFL Hackathon.

**This is the backend part of this project.**

## 项目架构
```
/wiseu-backend
    /app
        /api
            __init__.py
            endpoints.py  # 统一的API入口
        /models
            __init__.py
            user.py  # 用户相关模型
            course.py  # 课程表相关模型
            library.py  # 图书馆预约相关模型
            grades.py  # 成绩相关模型
            knowledge.py  # 知识库相关模型
        /services
            __init__.py
            user_service.py  # 用户服务
            course_service.py  # 课程服务
            library_service.py  # 图书馆预约服务
            grades_service.py  # 成绩服务
            knowledge_service.py  # 知识库服务
        /db
            __init__.py
            database.py  # 数据库连接与管理
        /llm
            __init__.py
            langchain_service.py  # LangChain集成
            llm_integration.py  # LLM服务与API接口的整合
        main.py  # FastAPI应用入口
    /tests
        test_api.py  # 单元测试
    requirements.txt  # 项目依赖
```
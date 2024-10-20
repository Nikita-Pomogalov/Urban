from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models.task import Task
from models.user import User
from schemas import CreateTask, UpdateTask, CreateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from starlette.status import HTTP_404_NOT_FOUND


router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(Task)).all()
    return users

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    tasks = db.scalar(select(Task).where(Task.id == task_id))
    if tasks is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    else:
        return tasks

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    db.execute(insert(Task).values(title=create_task.title, content=create_task.content,
                                   priority=create_task.priority, slug= slugify(create_task.title), user_id= user_id))
    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], tsk_user: UpdateTask, user_id: int):
    task = db.scalar(select(Task).where(Task.user_id == user_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(update(Task).where(Task.user_id == user_id).values(
        title=tsk_user.title, content=tsk_user.content,
        priority=tsk_user.priority, slug= slugify(tsk_user.title)
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], user_id: int, task_id: int):
    task = db.scalar(select(Task).where(Task.user_id == user_id))
    if task is None:
        task = db.scalar(select(Task).where(Task.id == task_id))
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Task was not found'
            )
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
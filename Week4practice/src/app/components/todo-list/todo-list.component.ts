import { Component, OnInit } from '@angular/core';

export interface Todo {
  id: number,
  content: string,
  completed: boolean,
} 

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {

  constructor() { }

  ngOnInit(): void { }

  onChange(id: number) {
    this.onToggle(id);
  }

  todos: Todo[] = [];
  inputTodo: string = '';

  onToggle(id: number) {
    let i = this.todos.findIndex(p => p.id === id);
    this.todos[i].completed = !this.todos[i].completed;
  }

  removeTask(id: number) {
    let i = this.todos.findIndex(p => p.id === id);
    this.todos.splice(i, 1);
  }

  addTodo() {
    if(this.inputTodo.trim()!=='') {
      this.todos.push(
        {id: this.todos.length, content: this.inputTodo, completed: false}
      );
      this.inputTodo = '';
    }
  }
}
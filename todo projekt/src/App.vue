<script setup lang="ts">
import { ref } from 'vue';
import { createApp } from 'vue';

type Todo = {
  id: number,
  text: string,
  isDone: boolean
}

const todoList = ref([] as Todo[])
const todoText = ref("")
const curID = ref(0)

function removeTodo(id: number) {
  todoList.value = todoList.value.filter((todo) => todo.id !== id)
}

function addTodo(todoText: string) {
  const latestID = todoList.value.slice(-1)[0]
  todoList.value.push({id: curID.value + 1, text: todoText, isDone: false})
  curID.value += 1;
}

</script>

<template>
  <h1>To-Do</h1>

  <div class="todoListe">
    <div class="inputField">
      <input class="inputText" v-model="todoText" type="text">
      <button id="submitButton" @click="addTodo(todoText)">Submit</button>
    </div>

    <p v-if="todoList.length==0" class="nothingTodo">Nichts zu tun</p>
    <div v-else>
      <div v-for="todo in todoList" :key="todo.id" :class="todo.isDone ? 'todoFieldDone' : 'todoField'">
        <input id="todoCheckbox" type="checkbox" v-model="todo.isDone">
        <p id="todo">{{ todo.text }}</p>
        <button id="remove" @click="removeTodo(todo.id)">0</button>
      </div>
    </div>
  </div>
</template>

<style>
  * {
    margin: 0;
    padding: 0
  }

  body {
    background-color: #7dd0e3;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif
  }

  h1 {
    text-align: center;
    font-size: 42px;
    color: white;
    border-bottom-style: solid;
    text-shadow: black 0 0 2px;
  }

  .todoListe {
    display: flex;
    margin-top: 10px;
    justify-content: center;
    flex-direction: column;
  }

  .todoListe .nothingTodo {
    margin: auto;
    border-style: solid;
    padding: 20px;
    border-color: #27ba5a;
    background-color: #30d96b;
    color: white;
    text-shadow: black 0 0 2px;
    border-radius: 10px;
  }

  .todoListe .inputField {
    margin: 50px auto

  }

  .todoListe .inputField .inputText {
    padding: 7px 15px;
    color: white;
    text-shadow: black 0 0 2px;
    border-color: #27ba5a;
    border-style: solid;
    background-color: #30d96b;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
  }

  .todoListe #submitButton {
    padding: 7px 15px;
    color:white;
    text-shadow: black 0 0 2px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    border-style: solid;
    border-color: #27ba5a;
    background-color: #30d96b;
    transition: all 0.1s;
  }

  .todoListe #submitButton:hover {
    cursor: pointer;
    background-color: #2ee86f;
    border-color: #2edb6a;
  }

  .todoListe #submitButton:active {
    transform:scale(0.97)
  }

  .todoListe .todoField {
    margin: 10px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
  }

  .todoListe .todoField #todo {
    border-style: solid;
    color: white;
    text-shadow: black 0 0 2px;
    background-color: #30d96b;
    font-size: 16px;
    border-color: #27ba5a;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    margin-left: 5px;
    padding: 2px 50px;
  }

  .todoListe .todoField #remove {
    padding: 3.5px 7px;
    color: transparent;
    background-color: #d62b2b;
    border-style: solid;
    border-color: #bd2b26;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    transition: all 0.1s;
}

  .todoListe .todoField #remove:hover {
    background-color: #e62c2c;
    border-color: #d4302a;
    cursor: pointer;
  }

  .todoListe .todoField #remove:active {
    transform: scale(0.97);
  }


    .todoListe .todoFieldDone {
    margin: 10px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
  }

  .todoListe .todoFieldDone #todo {
    border-style: solid;
    color: white;
    text-shadow: black 0 0 2px;
    text-decoration: line-through;
    background-color: #dbd3d3;
    font-size: 16px;
    border-color: #bdb5b5;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    margin-left: 5px;
    padding: 2px 50px;
  }

  .todoListe .todoFieldDone #remove {
    padding: 3.5px 7px;
    color: transparent;
    background-color: #d62b2b;
    border-style: solid;
    border-color: #bd2b26;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    transition: all 0.1s;
}

  .todoListe .todoFieldDone #remove:hover {
    background-color: #e62c2c;
    border-color: #d4302a;
    cursor: pointer;
  }

  .todoListe .todoFieldDone #remove:active {
    transform: scale(0.97);
  }

</style>
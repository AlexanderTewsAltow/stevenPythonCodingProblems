<script setup>
import NoteType from './components/NoteType.vue';

</script>


<template>
  <header>
   
  </header>

  <div class="noteTypesTab">
    <button>
      <i class=""></i>
    </button>
    <div class="noteTypes">
      <NoteType id=0 displayName="test" isSelected=true></NoteType>
      <NoteType id=1 displayName="also test" isSelected=true></NoteType>
    </div>
  </div>
</template>


<style>
.noteTypesTab {
  background-color: #1f1e1e;
  
  width: 20%;
  height: 97vh;
  overflow:hidden;
}
</style>

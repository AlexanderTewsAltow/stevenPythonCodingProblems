<script setup>


defineProps({
    id: {
        type: Number,
        required: true
    },
    displayName: {
        type: String,
        required: true
    },
    isSelected: {
        type: Boolean,
        required: true
    }
})
</script>


<template>
    <button class="defaultStyle">
        <span>{{displayName}}</span>
    </button>
</template>


<style>

.defaultStyle span {
    border-left-style: solid;
    border-color: #F9F9F9;
    border-width: 2px;
    padding-left: 10px;
}

.defaultStyle {
    display: flex;
    flex-direction: column;
    height: 40px;
    width: 97vh;
    margin-top: 5px;
    padding-left: 20px;
    background-color: transparent;
    background: #272626;

    color: #F9F9F9;
    font-size: 18px;
    justify-content: center;

    border-style: none;

    transition: 0.3s;
}

.defaultStyle:hover {
    background: #454343;
    cursor: pointer;
}

.defaultStyle:active {
    transition: 0.1s;
    font-size: 17px;
}

</style>
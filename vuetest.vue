<script>
export default {
    data() {
        return {
            count: 0
        }
    },

    methods: {
        increment() {
            this.count++
        },

        decrement() {
            this.count--
        }
    }
}
</script>


<template>

<button @click="increment">Increase count</button>
<button @click="decrement">Decrease count</button>
<p>Count: {{ count }}</p>

</template>
<script setup>
import {useToastStore} from '@/stores/toast'

const store = useToastStore()
</script>

<template>
  <div
      v-if="store.isVisible"
      :class="store.classes"
      class="transition ease-in-out delay-500 duration-500 px-6 py-6 fixed top-full right-8 rounded-xl shadow-xl"
  >
    {{ store.message }}
  </div>
</template>
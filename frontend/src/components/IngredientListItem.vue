<template>
    <div class="">
      <h3>{{ name }}</h3>
      <ul>
        <li>Fats: {{ fats }}</li>
        <li>Calories: {{ calories }}</li>
        <li>Proteins: {{ proteins }}</li>
        <li>Carbohydrates: {{ carbohydrates }}</li>
      </ul>
    </div>
  </template>
  
  <script>
    export default {
      props: {
        name: {
          type: String,
          required: true
        },
        fats: {
          type: Number,
          default: 0
        },
        calories: {
          type: Number,
          default: 0
        },
        proteins: {
          type: Number,
          default: 0
        },
        carbohydrates: {
          type: Number,
          default: 0
        }
      }
    };
  </script>
  
  <style>

  </style>
  
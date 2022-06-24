<script setup lang="ts">
import { stringifyStyle } from '@vue/shared';
import { ref } from 'vue';
/*
Todo:

- Rework whole "addedProductGroups" thingy -> isnt designed as planned (design on figma.com)
- Rework CSS design (so the two divs that are currently aligned vertically are aligned horizontally)
- Option to set amount of products you want to add
- Get rid of hardcoded groups & allow user to add custom group (incase if user needs a group that isnt specified)
  -> maybe leave some hardcoded groups in + allow user -,,-?
- Add button to remove products instead of letting user click on the text
- Replace "Placeholder" with listName

*/

const productsInList = ref([
  {
    group: "Obst",
    products: {
      [1]: {
        id: 1,
        name: "1x Luft",
        amount: 1,
        isPurchased: false
      },
      [2]: {
        id: 2,
        name: "1x Gold",
        amount: 1,
        isPurchased: false
      }
    }
  },
  {
    group: "Gemüse",
    products: {
      [1]: {
        id: 1,
        name: "1x Gemüse Luft",
        amount: 1,
        isPurchased: false
      }
    }
  }
])
const selectedGroup = ""
const productName = ""
let isButtonDisabled=false;
let listName = "Einkaufslistenname"

function setListName(newListName: string) {
  listName = newListName
  isButtonDisabled = true
}

function addProduct(productName: string, groupName: string) {

  productsInList.value.map((groups, groupIndex) => {

    if (groups.group == groupName) {

      Object.keys(groups.products).map((indexedProducts, productIndex) => {
        console.log("_","indexedProducts",indexedProducts,"productIndex",productIndex,"groups",groups,"groupIndex",groupIndex)
        console.log("ran")
        let theProduct = groups.products[parseInt(indexedProducts)]
        if (groups.products[parseInt(indexedProducts)].name.includes(productName)) {
          theProduct.amount += 1
          theProduct.name = theProduct.amount + "x " + productName
        } else {
          const latestID = Object.keys(groups.products).length + 1
          groups.products[latestID] = {
            id: latestID,
            name: "1x " + productName,
            amount: 1,
            isPurchased: false
          }
        }
        console.log("finished")
      })
    }
  })
}

function removeProduct(groupName: string,id: number) {
productsInList.value.forEach((indexedGroups) => {
  if (indexedGroups.group == groupName) {
    delete indexedGroups.products[id];
    console.log(indexedGroups.group, Object.keys(indexedGroups.products).length)
  }
}
)
  console.log(groupName, id)
}

</script>

<template>
  <h1>Einkaufsliste</h1>

  <div class="templateGroupA">
    <div class="setShoppingListName defaultBg">
      <input type="text" id="shoppingListName" v-model="listName" placeholder="Einkaufslistenname">
      <button id="setNameButton" class="defaultButton" @click="setListName(listName)">Festlegen</button>
    </div>

    <div class="addProduct defaultBg">
      <h2>Produkt hinzufügen</h2>
      <div class="addProductGroup">
        <input type="number" id="amount" placeholder="0">
        <input type="text" id="productName" v-model="productName" placeholder="Produktname eingeben">
        <select id="groups" v-model="selectedGroup">
          <option disabled value="">Gruppe</option>
          <option>Obst</option>
          <option>Gemüse</option>
        </select>
      </div>

      <button id="addProductButton" class="defaultButton" @click="addProduct(productName, selectedGroup)">Produkt hinzufügen</button>
    </div>

    <div class="addedProductsGroup defaultBg">
      <h2>Placeholder</h2>
      <div class="addedProducts">
        <div v-for="products in productsInList" :key="products.group" class="addedProductGroups">
          <h3 v-if="Object.keys(products.products).length > 0">{{ products.group }}</h3>
          <p v-for="allProducts in products.products" :key="allProducts.valueOf().id" :class="allProducts.valueOf().isPurchased ? 'productPurchased' : 'product'" @click="removeProduct(products.group,allProducts.valueOf().id)">{{allProducts.valueOf().name}}</p>
        </div>
      </div>

    </div>

  </div>
</template>

<style>
  * {
    margin: 0;
    padding: 0;
  }

  body {
    background-color: #F9F9F9;
    font-family: 'Jost';
  }

  input[type=number]::-webkit-inner-spin-button {
    -webkit-appearance: none;
  }

  .defaultBg {
    font-family: 'Jost';
    background-color: #EFEFEE;
    border-radius: 25px;
    border-style: solid;
    border-width: 1px;
  }

  .defaultButton {
    text-align: center;
    border-radius: 12px;
    border-width: 1px;
    font-family: 'Jost';
  }

  h1 {
    font-size: 58px;
    border-bottom-style: solid;
    border-width: 1px;
  }

  .templateGroupA {
    height: 400px;
    width: 1400px;
    padding-top: 30px;
    border-width: 1px;
    border-left-width: 0px;
    border-top-width: 0px;
    border-style: solid;
  }

  .setShoppingListName {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-left: 40px;
    width: 440px;
    height: 108px;
  }

  .setShoppingListName #shoppingListName {
    text-align: center;
    background-color: #D9D9D9;
    border-radius: 15px;
    border-width: 1px;
    height: 30px;
    width: 340px;
    margin-bottom: 15px;
  }

  .setShoppingListName #setNameButton {
    width: 340px;
    height: 25px;

    background-color: #16BA26;
    color: #F9F9F9;
    text-shadow: black 0 0 1px;
    
    transition: 0.1s;
  }

  .setShoppingListName #setNameButton:hover {
    background-color: #0ecf21;
  }

  .setShoppingListName #setNameButton:active {
    transform: scale(0.98);
  }

  .setShoppingListName #setNameButton:disabled {
    background-color: #c9c9c9;
  }

  .addProduct {
    display: flex;
    position: relative;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-left: 40px;
    margin-top: 116px;
    height: 150px;
    width: 440px;
  }

  .addProduct h2 {
    font-family: 'Jost';
    position: absolute;
    border-bottom-style: solid;
    width: 410px;
    padding-left: 30px;
    top: 0;
  }

  .addProduct #addProductButton {
    width: 10
  }

  .addProduct .addProductGroup {
    background-color: #D9D9D9;
    border-radius: 15px;
    height: 25px;
    width: 340px;
    margin-bottom: 20px;
  }

  .addProduct .addProductGroup #amount {
    background-color: transparent;
    height: 25px;
    width: 45px;
    text-align: center;
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
    border-width: 1px;
    border-right-width: 0px;
  }

  .addProduct .addProductGroup #productName {
    border-width: 1px;
    border-right-width: 0px;
    height: 25px;
    width: 220px;
    background-color: transparent;
    text-align: center;
  }

  .addProduct .addProductGroup #groups {
    background-color: transparent;
    height: 27px;
    border-width: 1px;
    border-top-right-radius: 15px;
    border-bottom-right-radius: 15px;
  }

  .addProduct #addProductButton {
    color:#F9F9F9;
    background-color: #16BA26;
    height:25px;
    width: 340px;
  }

  .addProduct #addProductButton:hover {
    background-color: #0ecf21;
    transition: 0.1s;
  }

  .addProduct #addProductButton:active {
    transform: scale(0.98);
  }

  .addedProductsGroup {
    height: 460px;
    width: 750px;
  }

  .addedProducts {
    display: flex;
    justify-content: space-around;
    border-style: solid;
  }

</style>

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
/*
savedProductsInList[0] -> Name für die Einkauslisten
savedProductsInList[1] -> Listen
savedProductsInList[1][X] -> x = gruppen
*/
const savedProductsInList = [
{
  [0]: {
    name: "TestList",
    id: 0
  },
  [1]: {
    name: "SecondTestLest",
    id: 1
  }
},
{
  [0]: [
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
  }
  ],

  [1]: [
    {
    group: "Obst",
    products: {
      [1]: {
        id: 1,
        name: "1x Test Luft",
        amount: 1,
        isPurchased: false
      },
      [2]: {
        id: 2,
        name: "1x Test Gold",
        amount: 1,
        isPurchased: false
      }
    }
  }
  ]
}
]


// Objects.keys(savedProductsInList.value['Einkaufslistenname']['listvalue']) -> zugriff auf gespeicherte daten (gruppen & deren produkte)
const selectedGroup = ""
const productName = ""
const amount = 1
let isButtonDisabled=ref(false);
let listName = ref("Einkaufslistenname")

function setListName(event: Event) {
  event.preventDefault();
  listName.value = event.target[0].value
  isButtonDisabled.value = true;
}

function saveList(){
  let newID = Object.keys(savedProductsInList[0]).length
  let newListName = listName.value
  let listvalue = productsInList.value
  savedProductsInList[0][newID] = {
    name: newListName,
    id: newID
  }

  savedProductsInList[1][newID] = productsInList.value
}

function loadList(id: string) {
  productsInList.value = savedProductsInList[1][id]
  listName.value = savedProductsInList[0][id].name
  console.log("called")
}

function deleteList(id: string) {
  if (!savedProductsInList[1][id]) return;
  delete savedProductsInList[1][id]
  productsInList.value = []
  listName.value = "Einkaufslistenname"
}

function conditionlessAddProduct(existsAlready: boolean, groupIndex: number, indexedProducts: string, productName: string, id: number, latestID: number, amount: number) {
  if(existsAlready === false) {
    productsInList.value[groupIndex].products[latestID] = {
      id: latestID,
      name: amount + "x " + productName,
      amount: amount,
      isPurchased: false
    }
  } else {
    let product = productsInList.value[groupIndex].products[parseInt(id)]
    console.log(product)
    product.amount += amount
    product.name = product.amount + "x " + productName
  }

  saveList()
}

function addProduct(productName: string, groupName: string, amount: number) {

  let found = false;
  let groupIndexP = 0;
  let indexedProductsP = "";
  let productNameP = "";
  let latestID = 0;
  let productIdP = 0;
  let amountP = 0;
  productsInList.value.map((groups, groupIndex) => {

    if (groups.group == groupName) {
      Object.keys(groups.products).map((indexedProducts, productIndex) => {
        let theProduct = groups.products[parseInt(indexedProducts)]

        if (groups.products[parseInt(indexedProducts)].name.includes(productName)) {
          console.log("found")
          found = true;
          productIdP = productIndex
        }
        groupIndexP = groupIndex
        indexedProductsP = indexedProducts
        productNameP = productName
        amountP = amount
        latestID = Object.keys(groups.products).length + 1
      })
    }
  })
  console.log(found, groupIndexP, indexedProductsP, productNameP, productIdP, latestID,amountP) 
  conditionlessAddProduct(found, groupIndexP, indexedProductsP, productNameP, productIdP+1, latestID, amountP)
}

function removeProduct(groupName: string,id: number) {
productsInList.value.forEach((indexedGroups) => {
  if (indexedGroups.group == groupName) {
    let product = indexedGroups.products[id]
    if(product.amount > 1) {
      product.amount -= 1
      let newname = product.name.split('x ').pop()
      console.log(newname)
      product.name = product.amount + "x " + newname
    } else {
    delete indexedGroups.products[id];
    }
  }
}
)
}

</script>

<template>
  <h1>Einkaufsliste</h1>

  <div class="templateGroupA">
    <div class="setShoppingListName defaultBg">
      <form class="shoppingListForm" @submit="setListName">
        <input type="text" id="shoppingListName" placeholder="Einkaufslistenname">
        <button :disabled="isButtonDisabled" id="setNameButton" class="defaultButton" type="submit">Festlegen</button>
      </form>
    </div>

    <div class="addProduct defaultBg">
      <h2>Produkt hinzufügen</h2>
      <div class="addProductGroup">
        <input type="number" id="amount" v-model="amount" placeholder="1">
        <input type="text" id="productName" v-model="productName" placeholder="Produktname eingeben">
        <select id="groups" v-model="selectedGroup">
          <option disabled value="">Gruppe</option>
          <option>Obst</option>
          <option>Gemüse</option>
        </select>
      </div>

      <button :disabled="!isButtonDisabled" id="addProductButton" class="defaultButton" @click="addProduct(productName, selectedGroup, amount)">Produkt hinzufügen</button>
    </div>

    <div class="addedProductsGroup defaultBg">
      <h2>{{ listName }}</h2>
      <div class="addedProducts">
        <div v-for="products in productsInList" :key="products.group" class="addedProductGroups">
          <h3 v-if="Object.keys(products.products).length > 0">{{ products.group }}</h3>
          <p v-for="allProducts in products.products" :key="allProducts.valueOf().id" :class="allProducts.valueOf().isPurchased ? 'productPurchased' : 'product'" @click="removeProduct(products.group,allProducts.valueOf().id)">{{allProducts.valueOf().name}}</p>
        </div>
      </div>
      <div class="containerB">
        <button id="saveList" class="defaultButton" @click="saveList">Speichern</button>
        <button id="deleteList" class="defaultButton" @click="deleteList(listnames.id)">Löschen</button>
      </div>
    </div>

    <div class="savedListsGroup defaultBg">
      <div v-for="lists in savedProductsInList" :key="lists" class="savedLists">
        <h3 v-for="listnames in lists" @click="loadList(listnames.id)">{{ listnames.name }}</h3>
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

  .setShoppingListName .shoppingListForm {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
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

  .setShoppingListName #setNameButton:hover:enabled {
    background-color: #0ecf21;
  }

  .setShoppingListName #setNameButton:active:enabled {
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

  .addProduct #addProductButton:disabled {
    background-color: #c9c9c9;
  }

  .addProduct #addProductButton:hover:enabled {
    background-color: #0ecf21;
    transition: 0.1s;
  }

  .addProduct #addProductButton:active:enabled {
    transform: scale(0.98);
  }

  .addedProductsGroup {
    justify-content: space-between;
    flex-direction: column;
    display: flex;
    height: 460px;
    width: 750px;
  }

  .addedProductsGroup h2 {
      border-bottom-style: solid;
      padding-left: 10px;
  }

  .addedProductsGroup #saveList {
    color:#F9F9F9;
    background-color: #3873d1;
    float: right;
    margin-right: 20px;
    margin-bottom: 20px;
    height: 25px;
    width: 100px;
  }


  .addedProductsGroup #saveList:hover:enabled {
    background-color: #4287f5;
    transition: 0.1s;
  }

  .addedProductsGroup #saveList:active:enabled {
    transform: scale(0.98)
  }

  .addedProductsGroup #deleteList {
    background-color: #fa3455;
    color: #F9F9F9;
    float: right;
    margin-right: 10px;
    height: 25px;
    width: 100px;
  }

  .addedProductsGroup #deleteList:hover {
    background-color: #d1304b;
    transition: 0.1s;
  }

  .addedProductsGroup #deleteList:active {
    transform: scale(0.98)
  }


  .addedProducts {
    display: flex;
    justify-content: space-around;
    border-style: solid;
  }

</style>

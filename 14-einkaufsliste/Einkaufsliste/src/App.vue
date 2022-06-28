<script setup lang="ts">
import { stringifyStyle } from '@vue/shared';
import { ref } from 'vue';
/*
Todo:
für wenn mir langweilig zu hause ist:
- Rework whole "addedProductGroups" thingy -> isnt designed as planned (design on figma.com)
- Rework CSS design (so the two divs that are currently aligned vertically are aligned horizontally)
- Get rid of hardcoded groups & allow user to add custom group (incase if user needs a group that isnt specified)
  -> maybe leave some hardcoded groups in + allow user -,,-?
- Add button to remove products instead of letting user click on the text
*/

const productsInList = ref([])
/*
savedProductsInList[0] -> Name für die Einkauslisten
savedProductsInList[1] -> Listen
savedProductsInList[1][X] -> x = gruppen
*/

// delete list: get loaded lists name, look in savedProdutsInList for the name and get the id, then delete it from the obj
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
  let newID = 0;
  let newListName = listName.value
  let found = false;
  Object.keys(savedProductsInList[0]).map((lists) => {
    if(savedProductsInList[0][lists].name == newListName) {
      newID = savedProductsInList[0][lists].id
      found = true;
    }
  })

  if(found == false) {
    console.log("creating new entry")
    newID = Object.keys(savedProductsInList[0]).length
    savedProductsInList[0][newID] = {
      name: newListName,
      id: newID
    }
  }

  savedProductsInList[1][newID] = productsInList.value
}

function loadList(id: string) {
  productsInList.value = savedProductsInList[1][id]
  listName.value = savedProductsInList[0][id].name
  console.log("called")
}

function deleteLoadedList() {
  let loadedListName = listName.value
  if (savedProductsInList[0].length != 0) {
  Object.keys(savedProductsInList[0]).map((lists) => {
    if (savedProductsInList[0][lists].name == listName.value) {
      delete savedProductsInList[0][lists]
      delete savedProductsInList[1][lists]
    }
  })
  }
  productsInList.value = []
  listName.value = "Einkaufslistenname"
  isButtonDisabled.value = false;

}

function conditionlessAddProduct(existsAlready: boolean, groupName: string, groupIndex: number, productName: string, id: number, latestID: number, amount: number) {
  if(existsAlready === false) {
    productsInList.value[groupIndex].products[latestID] = {
      id: latestID,
      name: amount + "x " + productName,
      amount: amount,
      isPurchased: false
    }
  } else {
    let product = productsInList.value[groupIndex].products[parseInt(id)]
    console.log(id)
    product.amount += amount
    product.name = product.amount + "x " + productName
  }
  console.log(productsInList.value[groupIndex])
}

function addProduct(productName: string, groupName: string, amount: number) {

  let foundGroup = false;
  let found = false;
  let groupIndexP = 0;
  let indexedProductsP = "";
  let productNameP = "";
  let latestID = 0;
  let productIdP = 0;
  let amountP = 0;

  if (productsInList.value.length == 0) {
    productsInList.value = [{
      group: groupName,
      products: {
        [0]: {
        id: 0,
        name: "",
        amount: 0,
        isPurchased: false
      }}
    }]
  }
  console.log(productsInList.value)
  productsInList.value.map((groups, groupIndex) => {

    if (groups.group == groupName) {
      foundGroup = true;
      Object.keys(groups.products).map((indexedProducts, productIndex) => {
        let theProduct = groups.products[parseInt(indexedProducts)]

        if (groups.products[parseInt(indexedProducts)].name.includes(productName)) {
          console.log("found")
          found = true;
          productIdP = productIndex
        }
        groupIndexP = groupIndex
      })
    latestID = Object.keys(groups.products).length
    }
  })
  productNameP = productName
  amountP = amount
  console.log(foundGroup)
  if(foundGroup == false) {
    groupIndexP = productsInList.value.length

    console.log("adding group",groupName, productName, amount)
    productsInList.value.push({
      group: groupName,
      products: {
        [0]: {
          id: 0,
          name: "",
          amount: 0,
          isPurchased: false
        }
      }
    })
  }

  //console.log(productsInList.value)
  //console.log(found, groupName, groupIndexP, productNameP, productIdP, latestID, amountP)
  console.log(productIdP)
  conditionlessAddProduct(found, groupName, groupIndexP, productNameP, productIdP, latestID, amountP)
  saveList()
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
    <div class="topGroup">
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
          <button id="deleteList" class="defaultButton" @click="deleteLoadedList">Löschen</button>
        </div>
      </div>
    </div>


  </div>
    <div class="savedListsGroup defaultBg">
      <div v-for="lists in savedProductsInList" :key="lists">
        <h3 v-for="listnames in lists" @click="loadList(listnames.id)" class="savedLists">{{ listnames.name }}</h3>
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
    height: 480px;
    width: 1400px;
    padding-top: 30px;
    border-width: 1px;
    border-left-width: 0px;
    border-top-width: 0px;
    border-style: solid;
  }

  .topGroup {
    display:flex;
    position: absolute;
  }

  .setShoppingListName {
    position: absolute;
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
    width: 270px;
    margin-bottom: 15px;
  }

  .setShoppingListName #setNameButton {
    width: 270px;
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
    margin-top: 166px;
    height: 150px;
    width: 440px;
  }

  .addProduct h2 {
    font-family: 'Jost';
    position: absolute;
    border-bottom-style: solid;
    width: 94%;
    padding-left: 20px;
    top: 0;
  }

  .addProduct .addProductGroup {
    background-color: #D9D9D9;
    border-radius: 15px;
    height: 25px;
    width: 310px;
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
    width: 190px;
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
    width: 310px;
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
    margin-left: 70px;
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

  .savedListsGroup {
    margin-top: 20px;
  }

  .savedLists {
    padding-left: 10px;
  }

</style>

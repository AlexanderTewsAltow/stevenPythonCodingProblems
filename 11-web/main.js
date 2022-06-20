function onClick() {
    const textAreaElement = document.querySelector("#myTextArea")
    const text = textAreaElement.value
    alert(text)
}

function onLoad() {
    document.querySelector("#myButton").addEventListener("click", onClick)
}

document.addEventListener("DOMContentLoaded", onLoad)
let addingButton=document.getElementById('add-btn');
let taskInput=document.getElementById('input-task');
let list=document.getElementById('list');

addingButton.addEventListener('click',addListItem);

load();

function addListItem() {
    let value=taskInput.value;

    if(value!==null && +value!==0 && value!==undefined) {
        taskInput.value='';
        createListItem(value);
    }  else {
        alert('Please, enter a valid task name!');
    }
}

function createListItem(value) {
    let listItem=document.createElement('li');
    let listItemCheckbox=document.createElement('input');
    let content=document.createElement('p');
    let image=document.createElement('img');

    listItem.classList='list-item';
    content.innerHTML=value;
    listItemCheckbox.setAttribute('type','checkbox');
    listItemCheckbox.setAttribute('onclick','checkIsDone(this)');

    image.setAttribute('src','https://cdn4.iconfinder.com/data/icons/web-ui-color/128/Close-128.png');
    image.setAttribute('onclick','deleteListItem(this.parentElement)');
    image.setAttribute('width','30');

    listItem.appendChild(listItemCheckbox);
    listItem.appendChild(content);
    listItem.appendChild(image);

    list.appendChild(listItem);
    save();
}

function checkIsDone(item) {
    if(item.checked) {
        item.parentElement.childNodes[1].style.textDecoration='line-through';
    } else {
        item.parentElement.childNodes[1].style.textDecoration='none';
    }
    save();
}

function deleteListItem(item) {
    item.remove();
    save();
}

function save() {
    localStorage.setItem('listItems',JSON.stringify(list.innerHTML));
}

function load() {
    let storage=JSON.parse(localStorage.getItem('listItems'));
    list.innerHTML=storage;

    //console.log(storage);
}
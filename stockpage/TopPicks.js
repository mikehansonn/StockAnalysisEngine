document.addEventListener('DOMContentLoaded', function() {
    const nameList = document.getElementById('stockList');
    const names = ["Jake", "Joe", "Todd", "Bill", "Smith"];
    names.forEach(name => {
        const listItem = document.createElement('li');
        listItem.textContent = name;
        nameList.appendChild(listItem);
    });
})
  
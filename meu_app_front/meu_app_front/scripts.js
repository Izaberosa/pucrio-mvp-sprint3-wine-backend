/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/bebida';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.bebidas.forEach(item => insertList(item.fixed_acidity, item.volatile_acidity, item.citric_acid, item.residual_sugar, item.chlorides, item.free_sulfurdioxide, item.total_sulfurdioxide, item.density, item.pH, item.sulphates, item.alcohol, item.quality))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()


/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputFixed_acidity, inputVolatile_acidity, inputVitric_acid, inputResidual_sugar, inputChlorides, inputFree_sulfurdioxide, inputTotal_sulfurdioxide, inputDensity, inputPH, inputSulphates, inputAlcohol) => {

  const formData = new FormData();
  formData.append('fixed_acidity', inputFixed_acidity);
  formData.append('volatile_acidity', inputVolatile_acidity);
  formData.append('citric_acid', inputVitric_acid);
  formData.append('residual_sugar', inputResidual_sugar);
  formData.append('chlorides', inputChlorides);
  formData.append('free_sulfurdioxide', inputFree_sulfurdioxide);
  formData.append('total_sulfurdioxide', inputTotal_sulfurdioxide);
  formData.append('density', inputDensity);
  formData.append('pH', inputPH);
  formData.append('sulphates', inputSulphates);
  formData.append('alcohol', inputAlcohol);

  let url = 'http://127.0.0.1:5000/bebida';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/bebida?nome=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = () => {
  let inputFixed_acidity = document.getElementById("newFixed").value;
  let inputVolatile_acidity = document.getElementById("newVolatile").value;
  let inputVitric_acid = document.getElementById("newCitric").value;
  let inputResidual_sugar = document.getElementById("newResidual").value;
  let inputChlorides = document.getElementById("newChlorides").value;
  let inputFree_sulfurdioxide = document.getElementById("newFree").value;
  let inputTotal_sulfurdioxide = document.getElementById("newTotal").value;
  let inputDensity = document.getElementById("newDensity").value;
  let inputPH = document.getElementById("newPh").value;
  let inputSulphates = document.getElementById("newSulphates").value;
  let inputAlcohol = document.getElementById("newAlcohol").value;

  if (inputFixed_acidity === '') {
    alert("digite um numero");
  } 
else if (inputVolatile_acidity === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputVitric_acid === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputResidual_sugar === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputChlorides === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputFree_sulfurdioxide === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputTotal_sulfurdioxide === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputDensity === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputPH === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputSulphates === '') {
  alert("Escreva o nome de um item!");
} 
else if (inputAlcohol === '') {
  alert("Escreva o nome de um item!");
}  else {
    insertList(inputFixed_acidity, inputVolatile_acidity, inputVitric_acid, inputResidual_sugar, inputChlorides, inputFree_sulfurdioxide, inputTotal_sulfurdioxide, inputDensity, inputPH, inputSulphates, inputAlcohol)
    postItem(inputFixed_acidity, inputVolatile_acidity, inputVitric_acid, inputResidual_sugar, inputChlorides, inputFree_sulfurdioxide, inputTotal_sulfurdioxide, inputDensity, inputPH, inputSulphates, inputAlcohol)
    alert("Dado adicionado!")
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (Fixed_acidity, Volatile_acidity, Vitric_acid, Residual_sugar, Chlorides, Free_sulfurdioxide, Total_sulfurdioxide, Density, PH, Sulphates, Alcohol, quality) => {
  var item = [Fixed_acidity, Volatile_acidity, Vitric_acid, Residual_sugar, Chlorides, Free_sulfurdioxide, Total_sulfurdioxide, Density, PH, Sulphates, Alcohol, quality]
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("newFixed").value = "";
  document.getElementById("newVolatile").value = "";
  document.getElementById("newCitric").value = "";
  document.getElementById("newResidual").value = "";
  document.getElementById("newChlorides").value = "";
  document.getElementById("newFree").value = "";
  document.getElementById("newTotal").value = "";
  document.getElementById("newDensity").value = "";
  document.getElementById("newPh").value = "";
  document.getElementById("newSulphates").value = "";
  document.getElementById("newAlcohol").value = "";

  removeElement()
}
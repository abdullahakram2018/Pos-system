var product_ids = [];
var unit_ids = [];
var item_price = {};
var quantity = [];
var total_price = 0;

function addItem(item_id, item_name, item_price,item_quantity,item_unit) {
  var tableBody = document.getElementById('summary-table-body');
  var tr = document.createElement('tr');

  var td_name = document.createElement('td');
  td_name.innerHTML = item_name;

  var td_unit = document.createElement('td');
  let inp = document.createElement('input');
      inp.value =item_unit;
      inp.className = 'form-control';

  var td_quantity = document.createElement('td');
  
  td_quantity.innerHTML = item_quantity;

  var td_price = document.createElement('td');
  td_price.setAttribute('class', 'text-right');
  td_price.innerHTML =  item_price * item_quantity;

  total_price += item_price * item_quantity;
  td_quantity.appendChild(x);

  tr.appendChild(td_name);
  td_unit.appendChild(inp);
  tr.appendChild(td_unit);
  tr.appendChild(td_quantity);
  tr.appendChild(td_price);

  clearTotal();

  tableBody.appendChild(tr);
  tableBody.appendChild(getTotal());

  product_ids.push(item_id);
  item_price.push(item_price);
  unit_ids.push(item_unit);
}

function clearAllItems() {
  var table = document.getElementById('summary-table-body');
  while (table.firstChild) {
    table.removeChild(table.firstChild);
  }

  product_ids = [];
  unit_ids = [];
  item_price = {};
  quantity = [];
  total_price = 0;

  table.appendChild(getTotal());
}

function clearTotal() {
  var total_tr = document.getElementById("total-tr");
  if (total_tr !== null) {
    total_tr.parentNode.removeChild(total_tr);
  }
}

function getTotal(){
  var tr_total = document.createElement('tr');
  tr_total.setAttribute('id', 'total-tr')

  var td_total_display = document.createElement('td');
  td_total_display.setAttribute('class', 'thick-line text-right');
  td_total_display.innerHTML = "<strong>Total: </strong>";

  var td_total_price = document.createElement('td');
  td_total_price.setAttribute('class', 'thick-line text-right');
  td_total_price.innerHTML = "<strong>$" + total_price + " </strong>";

  tr_total.appendChild(td_total_display);
  tr_total.appendChild(td_total_price);

  return tr_total;
}

function postOrder(url, cust_id) {
  data = {
    'customer_id' : cust_id,
    'product_ids' : product_ids,
    'unit_ids' : unit_ids,
    'item_price' : item_price,
    'quantity' : quantity,
    'total_price' : total_price,
  };

  let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0];

  let form = document.createElement('form');
  form.action = url;
  form.method = "POST";

  let inp = document.createElement('input');
  inp.type = 'hidden';
  inp.name = 'data';
  inp.value = JSON.stringify(data);

  form.appendChild(csrftoken);
  form.appendChild(inp);

  document.body.appendChild(form);
  form.submit();
}
function generatePDF(){
  const element = document.getElementById('pdf1');

  html2pdf()
  .from(element)
  .save();
}
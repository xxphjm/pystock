
export default function toward(data){
  
axios.post('http://localhost:8000/toward',Qs.stringify(data))
.then(res => {
  let response=res['data']
  console.log(response);
  let content=` 
  <div id="name"></div>
  <div class='col-7'>
  <div class="stock"></div></div>
  <div class='col-5'>
  <div class="toward"> </div>
  <div class="tail"> </div>
  </div>
  `
  $('#container').html(content);
  $('.toward').empty();
  
  response.count[0].slice(2,7).forEach((obj, index)=>{
    
    console.log(index, obj);
    var bar = `<div class="bar"><div class="text"></div></div>`;
    var element = $(bar);
    element.css("height", obj*20+"px");
    element.children('.text').text(obj);
    
    $(".toward").append(element);
    
  });
  
  let stock=`<img src="../static/img/${response.id}.png" alt="">`
  let idname=`<h3>${response.id}  ${response.name}</h3>`
  $('#name').html(idname);
  console.log(data)
  $('.stock').html(stock);
  let all= response['stock'][0]
  let tail=`<div class="tab btn-group special" role="group">
  <button class="btn-secondary border-0" onclick="openCity(event, 'Value')" id="defaultOpen">價值</button>
  <button class="btn-secondary border-0" onclick="openCity(event, 'Security')">安全</button>
  <button class="btn-secondary border-0" onclick="openCity(event, 'Growth')">成長</button>
  <button class="btn-secondary border-0" onclick="openCity(event, 'Bargaining')">籌碼</button>
  <button class="btn-secondary border-0" onclick="openCity(event, 'Technology')">技術</button>
  </div>
  <div id="Value" class="tabcontent">
  <div class='row'>
  <div class='col-10'>
  <ul class='content'>
  <li class='co'>10<=本益比(${all[6]})<20</li>
  <li class='co'>本淨比(${all[7]})<1.5</li>
  <li class='co'>近三年平均殖利率(${all[8]}%)>4%</li>
  </ul>
  </div>
  <div class='ic col-2'>
  <ul class='icon'></ul>
  </div>
  </div>
  </div>
  <div id="Security" class="tabcontent">
  <div class='row'>
  <div class='col-10'>
  <ul class='content'>
  <li class='co'>營業毛利率(${all[2]}%)>30%</li>
  <li class='co'>營益率(${all[3]}%)>10%</li>
  <li class='co'>負債比(${all[4]}%)<50%</li>
  <li class='co'>EPS(${all[5]}%)>0(元)</li>
  </ul>
  </div>
  <div class='ic col-2'>
  <ul class='icon'></ul>
  </div>
  </div>
  </div>
  <div id="Growth" class="tabcontent">
  <div class='row'>
  <div class='col-10'>
  <ul class='content'>
  <li class='co'>月增率(${all[9]}%)>5%</li>
  <li class='co'>年增率(${all[10]}%)>10%</li>
  <li class='co'>近12月營收成長(${all[11]}%)>15%</li>
  </ul>
  </div>
  <div class='ic col-2'>
  <ul class='icon'></ul>
  </div>
  </div>
  </div>
  <div id="Bargaining" class="tabcontent">
  <div class='row'>
  <div class='col-10'>
  <ul class='content'>
  <li class='co'>法人連2天買超</li>
  <li class='co'>主力連2天買超</li>
  <li class='co'>董監持股比例增加</li>
  </ul>
  </div>
  <div class='ic col-2'>
  <ul class='icon'></ul>
  </div>
  </div>
  </div>
  <div id="Technology" class="tabcontent">
  <div class='row'>
  <div class='col-10'>
  <ul class='content'>
  <li class='co'>股價在週線上</li>
  <li class='co'>股價在月線上</li>
  <li class='co'>股價在季線上</li>
  </ul>
  </div>
  <div class='ic col-2'>
  <ul class='icon'></ul>
  </div>
  </div>
  </div>`
  $('.tail').html(tail);

  
let good=`<li><img src="../static/img/good-review.png" alt="" width=80% height=80%></li>`
let bad=`<li><img src="../static/img/bad-review.png" alt="" width=80% height=80%></li>`
let sec=``

let Value=``;
let Growth=``;
let Technology=``;
let Bargaining=``;
 all.forEach(e => {
   let index=all.indexOf(e)
   console.log(index)
   switch (index) {
     case 3:
       if (all[index]>30) {
         sec+=good;
        
       }
       else{
         sec+=bad
       }
       break
     case 4:
      if (all[index]>10) {
        sec+=good;
       
      }
      else{
        sec+=bad
      }
      break
     case 5:
      if (all[index]<50) {
        sec+=good;
      }
      else{
        sec+=bad
      }

   break  
     case 6:
      if (all[index]>0) {
        sec+=good;
      }
      else{
        sec+=bad
      }

   break  
      case 7:
      if (all[index]<20) {
        Value+=good;
      }
      else{
        Value+=bad
      }

     break    
      case 8:
      if (all[index]<1.5){
        Value+=good;
      }
      else{
        Value+=bad
      }
      break      
      case 9:
      if (all[index]>4) {
        Value+=good;
      }
      else{
        Value+=bad
      }
     break      
     case 10:
      if (all[index]>5) {
        Growth+=good;
      }
      else{
        Growth+=bad
      }
      break     
       case 11:
       if (all[index]>10) {
         Growth+=good;
       }
       else{
         Growth+=bad
       }
       break
     case 12:
       if (all[index]>15) {
         Growth+=good;
       }
       else{
         Growth+=bad
       }
       break
     case 13:
       if (all[2]>all[index]) {
         Technology+=good;
       }
       else{
         Technology+=bad
       }
       break
     case 14:
       if (all[2]>all[index]) {
         Technology+=good;
       }
       else{
         Technology+=bad
       }
       break
     case 15:
       if (all[2]>all[index]) {
         Technology+=good;
       }
       else{
         Technology+=bad
       }
       break
     case 16:
       if (all[index]==1) {
         Bargaining+=good;
       }
       else{
         Bargaining+=bad
       }
       break
     case 17:
       if (all[index]==1) {
         Bargaining+=good;
       }
       else{
         Bargaining+=bad
       }
       break
     case 18:
       if (all[index]==1) {
         Bargaining+=good;
       }
       else{
         Bargaining+=bad
       }
       break
     default:
       break;
   }
  });
  console.log(sec)
  $('#Security').children('.row').children('.ic').children('.icon').html(sec);
  $('#Value').children('.row').children('.ic').children('.icon').html(Value);
  $('#Growth').children('.row').children('.ic').children('.icon').html(Growth);
  $('#Bargaining').children('.row').children('.ic').children('.icon').html(Bargaining);
  $('#Technology').children('.row').children('.ic').children('.icon').html(Technology);
  document.getElementById("defaultOpen").click();
$('#input').val('');

  })
  .catch(err => {
      console.error(err); 
  })
}
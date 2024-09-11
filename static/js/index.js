import startpage from './startpage.js'
import toward  from './toward.js'
$(document).ready(function () {
    
    $('#container').html(startpage());
    console.log('jbjj');
    axios.get('http://localhost:8000/select')
    .then(res => {
      
        let data=res['data']
        console.log(data)
        let str='<table class="table  table-hover" id="table"><thead><tr><th scope="col">股票代號</th><th scope="col">股票名稱</th><th scope="col">現價</th><th scope="col">股價淨值比</th><th scope="col">營業毛利率</th><th scope="col">營業利益率</th><th scope="col">負債比</th><th scope="col">每股盈餘</th><th scope="col">本益比</th><th scope="col">近三年殖利率</th></tr></thead>'
        data.forEach(e => {
            str+=`<tr><td id='id'>${e.有價證券代號}</td>
            <td>${e.有價證券名稱}</td>
            <td>${e.現價}</td>
            <td>${e.股價淨值比}%</td>
            <td>${e.營業毛利率}%</td>
            <td>${e.營業利益率}%</td>
            <td>${e.負債占資產比率}%</td>
            <td>${e.每股盈餘}%</td>
            <td>${e.本益比}%</td>
            <td>${e.近三年殖利率}%</td>
          
            </tr>`
        });
        str+='</table>'
        $('#content').append(str);
        $('#table').on('click','tr', function() {
        let name=$(this).children().eq(1).text()
        let data={
            'id': $(this).children().eq(0).text(),
        }
     
        console.log(data,name)
          toward(data,name)
        })
        $('#click').click(function (e) { 
            let data={
                'id': $('input').val()
            }
            console.log(data)
            toward(data)
        });

        $( ".table" ).DataTable({
            'searching':false,
            'info':false,
          });
  
        
    })
    .catch(err => {
        console.error(err); 
    })
   
});
export default function startpage() {
    const startpage=`
    
  <div class="re py-2 ">
    <div class="row d-flex align-items-center">
      <div class="col ">
        <figure class="remind p-1 rounded" style="border-left: .5rem solid 	#FFA042;border-right: .5rem solid 	#FFA042;">
          <blockquote class="blockquote ">
          <div class="condition">
          篩股條件<br>
          <ul class='re'>
              <li class='reco'>•本益比<20</li>
              <li class='reco'>•本淨比<1.5</li>
              <li class='reco'>•三年平均殖利率>4%</li>
              <li class='reco'>•毛利率>30%</li>
              <li class='reco'>•營益率>10%</li>
              <li class='reco'>•負債比<50% </li>
              <li class='reco'>•EPS>0 </li>
          </ul>
          
          </div>
          </blockquote>
          
        </figure>
      </div>
     
    </div>
  </div>


    <div id="content"></div>
   
    

    `;
    return startpage
}
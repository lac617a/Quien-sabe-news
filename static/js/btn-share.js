const btn_share = document.querySelectorAll('.share-all')
const news_redes = document.getElementById('redes')

const redes = [
  ['https://www.facebook.com/sharer/sharer.php?u=https://www.myruby.com.ar/','fab fa-facebook-f'],
  ['https://api.whatsapp.com/send?text=${msg} https://www.myruby.com.ar/','fab fa-whatsapp-square'],
]
function btnRedes (redes) {
  let formatRedes = `
                    <div class="col-lg-12 col-md-6 col-sm-4 text-center overlay-redes">
                      <button type="button" class="btn shadow m-2 btn-primary">
                        <a class="link-special-redes" href="${redes[0]}">
                          <i class="${redes[1]}"></i>
                          <span class="font-dark">Comparte con tus amigos!!</span>
                        </a>
                      </button>
                    </div>`
  return formatRedes
}
btn_share.forEach(item => {
  item.addEventListener('click',()=>{
    news_redes.style.display = 'block'
    const delete_btn = news_redes.innerHTML = '<button type="button" id="remove-redes" class="btn-close" aria-label="Close"></button>'
    let finalStr = ''
    for (let i in redes) {
      finalStr += btnRedes(redes[i])
      news_redes.innerHTML = delete_btn + finalStr
    }
  })
})

const wrapper = document.getElementById('wrapper')
const load = document.getElementById('load')

document.addEventListener('DOMContentLoaded',()=>{
  load.style.display = 'none'
  wrapper.classList.add('activate')
})

// Controlador de logo
const $logo_img = document.getElementById('t3-header')
// Controlador del navbar
const $navbar = document.getElementById('navbar__nav')

window.onscroll = function(){
  const currentScroll = document.documentElement.scrollTop
  if(currentScroll > 130){
    $logo_img.style.height = '179px'
    $navbar.classList.add('bg-activate')
  }
  else{
    $logo_img.style.height = '123px'
    $navbar.classList.remove('bg-activate')
  }
}

const URLApi = 'https://services.arcgis.com/BQTQBNBsmxjF8vus/ArcGIS/rest/services/Colombia_COVID19V/FeatureServer/6/query?where=1%3D1&outFields=NUEVOS_CASOS,TOTAL_CASOS,TOTAL_MUERTES,TOTAL_RECUPERADOS,NUEVOS_MUERTOS,NUEVO_RECUPERADOS&outSR=4326&f=json';
document.addEventListener('DOMContentLoaded',()=>{callApi();});

const app_covid = document.getElementById('app-covid')

async function callApi () {
  const call = await fetch(URLApi).then(response => response.json()).then(data => onSuccessResponse(data)).catch(err => console.error(err));
};

const COVID_CASE_NAME = {}

const onSuccessResponse = (data) => {
  const {
    fields,
    features
  } = data;
  fields_alias(fields)
  features_current_case(features)
}

function fields_alias (data) {
  for(alia of data){
    COVID_CASE_NAME[alia.name] = ''
  };
};
const features_current_case = (data) => {
  // [{NUEVOS_CASOS,NUEVOS_MUERTOS,NUEVO_RECUPERADOS,TOTAL_CASOS,TOTAL_MUERTES,TOTAL_RECUPERADOS}]
  for(current of data) {
    const new_case = current.attributes
    COVID_CASE_NAME['NUEVOS_CASOS'] = new_case.NUEVOS_CASOS
    COVID_CASE_NAME['NUEVOS_MUERTOS'] = new_case.NUEVOS_MUERTOS
    COVID_CASE_NAME['NUEVO_RECUPERADOS'] = new_case.NUEVO_RECUPERADOS
    COVID_CASE_NAME['TOTAL_CASOS'] = new_case.TOTAL_CASOS
    COVID_CASE_NAME['TOTAL_MUERTES'] = new_case.TOTAL_MUERTES
    COVID_CASE_NAME['TOTAL_RECUPERADOS'] = new_case.TOTAL_RECUPERADOS
  }
  innertList(COVID_CASE_NAME)
  // console.log(COVID_CASE_NAME)
};


function group_list (case_name,current_case) {
  return `<ol class="list-group list-group-numbered">
            <li class="list-group-item d-flex justify-content-between align-items-start">
              <div class="ms-1 me-auto">
                <div class="fw-bold">${case_name}</div>
              </div>
              <span class="badge bg-primary rounded-pill">${current_case}</span>
            </li>
          </ol>`
}

//! ANDAMOS SOLUCIONANDO ESTO DE AQUI ASI QUE TE ACUERDAS

function innertList (obj) {
  const arr = [obj]
  for(let value=0; value<=arr.length;value++){
    const key = Object.keys(obj)
    console.log(key)
  }
  // let loop_for_obj = ''
  // loop_for_obj += group_list('hola','vamos bien')
}
import {ref} from 'vue'

const getReportMetric = (metric) =>{
    const reportmetrics = ref ([])
    const error = ref (null)

    const load = async () =>{
        try{
            let data = await fetch ('http://127.0.0.1:8000/report/' + metric)
            console.log(data)
            if (!data.ok){
                throw Error('no data available')

            }
            reportmetrics.value = await data.json()
        }
            catch (err){
                error.value = err.message
                console.log (error.value)
            }
        }
        return (reportmetrics, error, load)
    }

export default getReportMetric
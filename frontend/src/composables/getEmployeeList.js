import {ref} from 'vue'

const getEmployeeList = () =>{
    const employees = ref ([])
    const error = ref (null)

    const load = async () =>{
        try{
            let data = await fetch ('http://127.0.0.1:8000/employee')
            console.log(data)
            if (!data.ok){
                throw Error('no data available')

            }
            employees.value = await data.json()
        }
            catch (err){
                error.value = err.message
                console.log (error.value)
            }
        }
        return (employees, error, load)
    }

export default getEmployeeList
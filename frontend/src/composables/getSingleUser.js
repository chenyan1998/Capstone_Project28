import {ref} from 'vue'

const getSingleUser = () =>{
    const singleuser = ref ([])
    const error = ref (null)

    const load = async () =>{
        try{
            let data = await fetch ('http://127.0.0.1:8000/user/60bdb77c4b2ec88180c75d54')
            console.log(data)
            if (!data.ok){
                throw Error('no data available')
            }
            singleuser.value = await data.json()
        }
            catch (err){
                error.value = err.message
                console.log (error.value)
            }
        }
        return (singleuser, error, load)
    }

export default getSingleUser
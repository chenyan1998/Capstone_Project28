<script>
// PUT to the resource with id = 5 to change the name of task


fetch('/127.0.0.1:8000/employee/', {
method: 'PUT',
body: JSON.stringify({
userId: 1,
id: 5,
title: "hello task",
completed: false
}),
headers: {
"Content-type": "application/json; charset=UTF-8"
}
})

.then(response => response.json())
.then(json => console.log(json))
/* will return
{
“userId”: 1,
“id”: 5,
“title”: “hello task”,
“completed”: false
}
*/

</script>
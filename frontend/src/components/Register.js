import React from 'react';

const Register = ()=>{
	const handleSubmit = (e) =>{
		e.preventDefault();
		var url = 'http://localhost:8000/register';
		console.log(JSON.stringify({username : e.target.username.value}));
		fetch (url, {
			method : 'POST',
			headers : {
			  'Content-type' : 'application/json',
			},
			body : JSON.stringify({username : e.target.username.value})
		  }).then ((response) => {
			if (response.status === 200){
				console.log(response.json());
		// 	  let expires = new Date()
		// 	  console.log(expires.getTime())
		//   expires.setTime(expires.getTime() + 1*1000*60*60*60*10)
		// 	  setCookie('token', response., { path: '/',  expires })
		// 	  history.push("/menu");
			}
			else{
			  console.log('error'+response);
			}
	});
}

	return(
		<>
			<form onSubmit = {handleSubmit}>
				<label>Register with a username</label>
				<input type="text" name="username"/>
				<input type="submit"/>
			</form>
		</>
	)
}

export default Register;
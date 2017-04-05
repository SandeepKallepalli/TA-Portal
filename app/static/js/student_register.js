$("#student_register_button").click(
	function(){
	var email = $("#student_register_email").val();
	var name = $("#student_register_name").val();
	var password = $("#student_register_password").val();
	var cgpa = $("#student_register_cgpa").val();
	var rollno =$("#student_register_rollno").val();		
	
	if(password.length <= 7)
	alert("password should be atleast 8 charecters long");
	
	if(Number(cgpa)<0 && Number(cgpa) >10)
	alert("Enter a valid cgpa");
	
	if(rollno >= 20110000 && rollno <= 20169999)
	rollno = rollno;
	else
	alert("Enter valid roll number");
	
	callstudent_register_function(email,name,rollno,password,cgpa);
	
			}
	
	
	
	);


var callstudent_register_function=function(email,name,rollno,password,cgpa)
			{
			 $.ajax({
                url : 'http://127.0.0.1:8080/student/register',
                method:"post",
                data:{
                        rollno:rollno,
                        name:name,
                        email:email,
			password:password,
			cgpa:cgpa,
                        },
                success:function(student,message){
                alert("student added");
		console.log(student);

                },
                error: function(xhr,status,error){
                alert("request failed");
		console.log(error);	
				},
                }
        );


			}



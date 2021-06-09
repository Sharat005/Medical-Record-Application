<template>
  <div>
  <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <a class="navbar-brand" href="#">BCC</a>
  <ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#">Home</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Screen</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">About</a>
    </li>
  </ul>
  </nav>  
  <body class="bg">
    <div class="container h-100">
        <div class="row h-100 pt-4 justify-content-center align-items-center">
            
            <div class="col-12 col-md-10 col-lg-8 form">
                <!-- Form -->
                <form class="form-example" action="">
                    <h1 class="text-center">BCC Survey Form</h1>
                    <p class="text-center" id="description">Thank you for taking the time to contribute to the Research</p>
                    <!-- Input fields -->
                    <div class="form-row">
                      <div class="form-group col-md-8">
                        <label for="inputEmail4" class="required">First Name:</label>
                        <input type="text" class="form-control" v-model="user.first_name" placeholder="Enter FirstName">
                      </div>
                      <div class="form-group col-md-4"> 
                        <label for="inputPassword4">Middle Name:</label>
                        <input type="name" class="form-control" v-model="user.middle_name" placeholder="Middle Name">
                      </div>
                    </div>
                    <div class="form-row">
                      <div class="form-group col-md-8">
                          <label for="name" class="required">Last Name:</label>
                          <input type="name" class="form-control" v-model="user.last_name" placeholder="Enter Last Name" id="name">
                      </div>
                      <div class="form-group col-md-4">
                          <label for="name">Date of Birth:</label>
                          <input type="date" class="form-control" v-model="user.dob" placeholder="Enter DOB" id="name">
                      </div>
                    </div>
                    <div class="form-row">
                      <div class="form-group col-md-6">
                          <label for="email" class="required">Email address:</label>
                          <input type="email" class="form-control" v-model="user.email" placeholder="Enter email" id="email">
                      </div>    
                      <div class="form-group col-md-6">
                          <label for="number">Number:</label>
                          <input type="number" class="form-control" v-model="user.phone" placeholder="Enter number" id="number">
                      </div>
                    </div>
                    <div class="form-row">
                      <div class="form-group">
                              <label for="gender" class="required">Gender:</label>

                      <div class="form-check col-md-4">
                          <input class="form-check-input" type="radio" name="name" id="Male" @change="genderChange('male')" value="option1">
                          <label class="form-check-label" for="Male">
                            Male
                          </label>
                        </div>
                        <div class="form-check col-md-4">
                          <input class="form-check-input" type="radio" name="name" id="Female" @change="genderChange('female')" value="option2">
                          <label class="form-check-label" for="Female">
                            Female
                          </label>
                        </div>
                        <div class="form-check col-md-4">
                          <input class="form-check-input" type="radio" name="name" id="Other" @change="genderChange('other')" value="option3">
                          <label class="form-check-label" for="Other">
                          Other
                          </label>
                        </div>
                      </div>
                    </div>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label for="dropdown">Race</label>
                          <select id="dropdown" v-model="user.race" class="form-control">
                            <option selected>Choose...</option>
                            <option value="AL">American Indian/Alaskan Native</option>
                            <option value="AL">Asian</option>
                            <option value="AL">Black/African American</option>
                            <option value="AL">Native Hawaiian/Pacific Islander</option>
                            <option value="AL">White</option>
                            <option value="AL">Other</option>
                          </select>
                  </div>
                  <div class="form-group col-md-6">
                    <label for="dropdown">Ethnicity</label>
                          <select id="dropdown" v-model="user.ethnicity" class="form-control">
                            <option selected>Choose...</option>
                            <option value="AL">Hispanic/Latino</option>
                            <option value="AL">Not Hispanic/Latino</option>
                            <option value="AL">Unknown</option>
                          </select>
                  </div>
                </div>
                <div class="form-group">
                        <label for="name">Address:</label>
                        <input type="address" class="form-control" v-model="user.address" placeholder="Enter address" id="address">
                </div>
                <div class="form-group">
                        <label for="name">City:</label>
                        <input type="city" class="form-control" v-model="user.city" placeholder="Enter City" id="city">
                </div>
                <div class="form-group">
                        <label for="dropdown">State</label>
                        <select id="dropdown" v-model="user.state" class="form-control">
                          <option selected>Choose...</option>
                          <option value="AL">Alabama</option>
                          <option value="AK">Alaska</option>
                          <option value="AZ">Arizona</option>
                          <option value="AR">Arkansas</option>
                          <option value="CA">California</option>
                          <option value="CO">Colorado</option>
                          <option value="CT">Connecticut</option>
                          <option value="DE">Delaware</option>
                          <option value="DC">District Of Columbia</option>
                          <option value="FL">Florida</option>
                          <option value="GA">Georgia</option>
                          <option value="HI">Hawaii</option>
                          <option value="ID">Idaho</option>
                          <option value="IL">Illinois</option>
                          <option value="IN">Indiana</option>
                          <option value="IA">Iowa</option>
                          <option value="KS">Kansas</option>
                          <option value="KY">Kentucky</option>
                          <option value="LA">Louisiana</option>
                          <option value="ME">Maine</option>
                          <option value="MD">Maryland</option>
                          <option value="MA">Massachusetts</option>
                          <option value="MI">Michigan</option>
                          <option value="MN">Minnesota</option>
                          <option value="MS">Mississippi</option>
                          <option value="MO">Missouri</option>
                          <option value="MT">Montana</option>
                          <option value="NE">Nebraska</option>
                          <option value="NV">Nevada</option>
                          <option value="NH">New Hampshire</option>
                          <option value="NJ">New Jersey</option>
                          <option value="NM">New Mexico</option>
                          <option value="NY">New York</option>
                          <option value="NC">North Carolina</option>
                          <option value="ND">North Dakota</option>
                          <option value="OH">Ohio</option>
                          <option value="OK">Oklahoma</option>
                          <option value="OR">Oregon</option>
                          <option value="PA">Pennsylvania</option>
                          <option value="RI">Rhode Island</option>
                          <option value="SC">South Carolina</option>
                          <option value="SD">South Dakota</option>
                          <option value="TN">Tennessee</option>
                          <option value="TX">Texas</option>
                          <option value="UT">Utah</option>
                          <option value="VT">Vermont</option>
                          <option value="VA">Virginia</option>
                          <option value="WA">Washington</option>
                          <option value="WV">West Virginia</option>
                          <option value="WI">Wisconsin</option>
                          <option value="WY">Wyoming</option>
                        </select>
                </div>
                <div class="form-group">
                    <label for="number" class="required">Zipcode:</label>
                    <input type="number" class="form-control" v-model="user.zipcode" placeholder="Enter Zipcode" id="number">
                </div>
                
                <div class="form-group">
                  <div class="col-md-4">
                    <button type="button" @click="submit()" class="btn btn-primary">Next</button>
                  </div>
                </div>
                
                    <!-- End input fields -->
                    <p class="copyright">&copy; Bootstrap 4 Survey Form by <a href="https://github.com/sharat005">Sharat</a>.</p>
                </form>
                <!-- Form end -->
            </div>
        </div>
    </div>
  </body>
  </div>
</template>

<script>

import axios from 'axios';
import _ from 'lodash';
import router from '@/router';
import Swal from 'sweetalert2'

// CommonJS

export default {
  name: 'HelloWorld',
  data () {
    return {
      user: {
        first_name: '',
        middle_name: '',
        last_name: '',
        dob: null,
        gender: '',
        email: '',
        phone: null,
        race: '',
        ethnicity: '',
        address: '',
        city: '',
        state: '',
        zipcode: '',
      },
    }
  },
  created() {
    
  },
  methods: {
    genderChange(gender) {
      this.user.gender = gender;
    },
    validate() {
      if(_.isEmpty(this.user.email)) {
        Swal.fire({
          title: 'Error!',
          text: 'Email Id is mandatory',
          icon: 'error',
          confirmButtonText: 'Ok'
        })
        return false
      }
      if(_.isEmpty(this.user.first_name)) {
        Swal.fire({
          title: 'Error!',
          text: 'First_name is mandatory',
          icon: 'error',
          confirmButtonText: 'Ok'
        })
        return false
      }
      if(_.isEmpty(this.user.last_name)) {
        Swal.fire({
          title: 'Error!',
          text: 'Last name is mandatory',
          icon: 'error',
          confirmButtonText: 'Ok'
        })
        return false
      }
      if(_.isEmpty(this.user.zipcode)) {
        Swal.fire({
          title: 'Error!',
          text: 'Zipcode is mandatory',
          icon: 'error',
          confirmButtonText: 'Ok'
        })
        return false
      }
      if(_.isEmpty(this.user.gender)) {
        Swal.fire({
          title: 'Error!',
          text: 'Gender is mandatory',
          icon: 'error',
          confirmButtonText: 'Ok'
        })
        return false
      }
      return true
    },
    // axios backend call to post the information filled in Page 1
    async submit() {
      console.log('user object before sending-----', _.cloneDeep(this.user.email));
      const valid = this.validate();
      if(valid) {
        await axios({
          method:'post',
          url: 'http://127.0.0.1:8000/api/user/users/',
          data: this.user,
          auth: { // Basic authentication
            username: 'sharatnaik',
            password: '12345678'
          }
        }).then((response) => {
          console.log("Response from the POST Method", response)
          Swal.fire({
          title: 'Error!',
          text: 'One user can fill only 3 records',
          icon: 'error',
          confirmButtonText: 'Ok'
        })

          // let newTask = {'id': response.data.id, 'description': this.description, 'status': this.status}

          // this.tasks.push(newTask)

          // this.description = '' // Reset description
          // this.status = 'todo' // Reset status
        })
        .catch((error) => {
          console.log(error);
        });
        router.push({ name: 'Screen', params: { email: this.user.email, zipcode: this.user.zipcode } });
      }
    },
  }
}
</script>

<style>
.bg {
    width: 100%;  
    min-height: 100vh;
  background: #FFFFFF;
}
.form {
    background-color: rgb(128, 6, 6);
    border: 1px solid black;
    border-radius: 12px;
    overflow: hidden;
}
.required:after {
    content:" *";
    color: red;
}
</style>
<template>
  <div class="new">
    <div v-if="eligible=='true'" class="card">
      <h5 class="card-header text-white bg-primary mb-3">Eligibility</h5>
      <div class="card-body bg-light mb-3">
        <h5 class="card-title">Yes, you are eligible to take part in the Research</h5>
        <p class="card-text">
          Thanks for taking the time to fill up the form and volunteering.
        </p>
      </div>
    </div>
    <div v-if="eligible=='false'" class="card">
      <h5 class="card-header text-white bg-danger mb-3">Eligibility</h5>
      <div class="card-body bg-light mb-3">
        <h5 class="card-title">Sorry, Unfortunately you are not allowed to take part in the Research</h5>
        <p class="card-text">
          Thanks for taking the time to fill up the form and volunteering.
        </p>
      </div>
    </div>
    <br>
    <br>
    <div>
      <h2>Recent Covid-19 Information of your area</h2>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// import _ from "lodash";
// import router from "@/router";

export default {
  name: "Eligibility",
  props: ['eligible', 'zipcode'],
  data() {
    return {
    };
  },
  created() {
    console.log('zipcode', this.zipcode);
  },
  methods: {
    genderChange(gender) {
      this.user.gender = gender;
    },
    // axios backend call to post the information filled in Page 1
  },
};
</script>

<style>
.bg {
  width: 100%;
  min-height: 100vh;
  background: #a64bf4;
  background: -webkit-linear-gradient(45deg, #00dbde, #fc00ff);
  background: -o-linear-gradient(45deg, #00dbde, #fc00ff);
  background: -moz-linear-gradient(45deg, #00dbde, #fc00ff);
  background: linear-gradient(45deg, #00dbde, #fc00ff);
}
.form {
  background-color: white;
  border: 1px solid black;
  border-radius: 12px;
  overflow: hidden;
}
.required:after {
  content: " *";
  color: red;
}
</style>
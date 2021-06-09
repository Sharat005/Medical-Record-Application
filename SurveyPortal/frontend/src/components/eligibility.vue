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
    <br>
    <form v-if="zipcode=='60601'">
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of cases : 1100</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Number of deaths : 12</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Death Rate : 81.9</label>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of tests : 29444</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Population : 14675</label>
        </div>
      </div>
    </form>
    <form v-if="zipcode=='60612'">
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of cases : 2433</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Number of deaths : 49</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Death Rate : 142.8</label>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of tests : 36655</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Population : 34311</label>
        </div>
      </div>
    </form>
    <form v-if="zipcode=='60602'">
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of cases : 90</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Number of deaths : 5</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Death Rate : 60</label>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of tests : 4690</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Population : 1244</label>
        </div>
      </div>
    </form>
    <form v-if="zipcode=='60607'">
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of cases : 2691</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Number of deaths : 12</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Death Rate : 16.9</label>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of tests : 28829</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Population : 29591</label>
        </div>
      </div>
    </form>
    <form v-else>
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of cases : 1991</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Number of deaths : 35</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Death Rate : 71</label>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="inputEmail4">Number of tests : 29829</label>
        </div>
        <div class="col">
          <label for="inputEmail4">Population : 24571</label>
        </div>
      </div>
    </form>
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
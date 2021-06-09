<template>
  <div class="top">
    <head>
      <title>Screening</title>
    </head>
    <body class="bg">
      <div class="container h-100 bg">
        <div class="row h-100 pt-4 justify-content-center align-items-center">
          <div class="col-12 col-md-10 col-lg-8 form">
            <!-- Form -->
            <form class="form-example" action="">
              <h1 class="text-center">Screening Form</h1>
              <p class="text-center" id="description">
                Thank you for taking the time to contribute to the Research
              </p>
              <!-- Input fields -->
              
              <div class="form-row">
                <div class="form-group">
                  <label for="gender"
                    >Has a doctor told you that you have Chronic Obstructive
                    Pulmonary Disease (COPD)?</label
                  >

                  <div class="form-check col-md-4">
                    <input
                      class="form-check-input"
                      type="radio"
                      id="copd"
                      v-model="copd"
                      @change="toggleRadio('copd', true)"
                      :value="true"
                    />
                    <label class="form-check-label" for="Male"> Yes </label>
                  </div>
                  <div class="form-check col-md-4">
                    <input
                      class="form-check-input"
                      type="radio"
                      id="copd"
                      v-model="copd"
                      @change="toggleRadio('copd', false)"
                      :value="false"
                    />
                    <label class="form-check-label" for="Female"> No </label>
                  </div>
                </div>
              </div>
              <div v-show="copd" class="form-row">
                <div class="form-group">
                  <label for="gender"
                    >Have you had a COPD exacerbation (flare-up) requiring treatment within the last 6 weeks?</label
                  >

                  <div class="form-check col-md-4">
                    <input
                      class="form-check-input"
                      type="radio"
                      id="copd_flare"
                      v-model="copd_flare"
                      @change="toggleRadio('copd_flare', true)"
                      :value="true"
                    />
                    <label class="form-check-label" for="Male"> Yes </label>
                  </div>
                  <div class="form-check col-md-4">
                    <input
                      class="form-check-input"
                      type="radio"
                      id="copd_flare"
                      v-model="copd_flare"
                      @change="toggleRadio('copd_flare', false)"
                      :value="false"
                    />
                    <label class="form-check-label" for="Female"> No </label>
                  </div>
                </div>
              </div>
              <div class="form-row">
                <div class="form-group">
                  <label for="gender"
                    >Have you ever smoked cigarettes?</label
                  >

                  <div class="form-check col-md-4">
                    <input
                      class="form-check-input"
                      type="radio"
                      id="smoked"
                      v-model="smoked"
                      @change="toggleRadio('smoked', true)"
                      :value="true"
                    />
                    <label class="form-check-label" for="Male"> Yes </label>
                  </div>
                  <div class="form-check col-md-4">
                    <input
                      class="form-check-input"
                      type="radio"
                      id="smoked"
                      v-model="smoked"
                      @change="toggleRadio('smoked', false)"
                      :value="false"
                    />
                    <label class="form-check-label" for="Female"> No </label>
                  </div>
                </div>
              </div>
              <div v-show="smoked" class="form-group">
                <label for="name">How old were you when you first started regular cigarette smoking?</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="smoking_start_age"
                  placeholder="Enter age"
                  id="address"
                />
              </div>
              <div v-show="smoked" class="form-group">
                <label for="name">If you stopped smoking cigarettes completely, how old were you when you stopped?</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="smoking_stop_age"
                  placeholder="Enter age"
                  id="address"
                />
              </div>
              <div v-show="smoked" class="form-group">
                <label for="name">On the average of the entire time you smoked, how many cigarettes do/did you smoke per day? 

(20 cigarettes = 1 pack)?</label>
                <input
                  type="number"
                  class="form-control"
                  v-model="smoke_count"
                  placeholder="Enter number"
                  id="address"
                />
              </div>
              <div class="form-group">
                <label for="gender"
                  >Are you using any blood pressure medicines?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="bp_medicine"
                    v-model="bp_medicine"
                    @change="toggleRadio('bp_medicine', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="bp_medicine"
                    v-model="bp_medicine"
                    @change="toggleRadio('bp_medicine', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div v-show="bp_medicine" class="form-group">
                <label for="name">Please list the blood pressure medicine you currently use</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="bp_medicine_list"
                  placeholder="Enter medicines"
                  id="address"
                />
              </div>
              <div class="form-group">
                <label for="gender"
                  >C1. (FEMALES ONLY) Are you pregnant, breast-feeding, or planning to become pregnant in the next 3 months?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="pregnant"
                    v-model="pregnant"
                    @change="toggleRadio('pregnant', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="pregnant"
                    v-model="pregnant"
                    @change="toggleRadio('pregnant', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="gender"
                  >C2. Have you received a course of antibiotics or systemic steroids for respiratory infection within the past 4 weeks?
</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="antibiotics"
                    v-model="antibiotics"
                    @change="toggleRadio('antibiotics', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="antibiotics"
                    v-model="antibiotics"
                    @change="toggleRadio('antibiotics', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="gender"
                  >C3. Do you have a history of asthma?
</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="asthma"
                    v-model="asthma"
                    @change="toggleRadio('asthma', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="asthma"
                    v-model="asthma"
                    @change="toggleRadio('asthma', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="name">Please provide age when diagnosed</label>
                <input
                  type="number"
                  class="form-control"
                  v-model="ashthma_age"
                  placeholder="Enter age"
                  id="age"
                />
              </div>
              <div class="form-group">
                <label for="gender"
                  >C4. Do you have a history of lung disease?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="lung_disease"
                    v-model="lung_disease"
                    @change="toggleRadio('lung_disease', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="lung_disease"
                    v-model="lung_disease"
                    @change="toggleRadio('lung_disease', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="name">Please specify</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="lung_disease_desc"
                  id="city"
                />
              </div>
              <div class="form-group">
                <label for="gender"
                  >C5. Do you have Diabetes Type I?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="diabetes"
                    v-model="diabetes"
                    @change="toggleRadio('diabetes', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="diabetes"
                    v-model="diabetes"
                    @change="toggleRadio('diabetes', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="gender"
                  >C6. Do you have lung cancer or a history of lung cancer?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="lung_cancer"
                    v-model="lung_cancer"
                    @change="toggleRadio('lung_cancer', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="lung_cancer"
                    v-model="lung_cancer"
                    @change="toggleRadio('lung_cancer', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="gender"
                  >C7. Do you have narrow-angle glaucoma, bladder-neck obstruction or severe renal impairment or urinary retention?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="glaucome"
                    v-model="glaucome"
                    @change="toggleRadio('glaucome', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="glaucome"
                    v-model="glaucome"
                    @change="toggleRadio('glaucome', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="gender"
                  >C8. Are you currently or have you in the past 30 days participated in any other clinical trials involving an investigational drug?
</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="clinical_trail"
                    v-model="clinical_trail"
                    @change="toggleRadio('clinical_trail', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="clinical_trail"
                    v-model="clinical_trail"
                    @change="toggleRadio('clinical_trail', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="gender"
                  >AF1. Do you have a history of atrial fibrillation?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="atrial"
                    v-model="atrial"
                    @change="toggleRadio('atrial', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="atrial"
                    v-model="atrial"
                    @change="toggleRadio('atrial', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div v-show="atrial" class="form-group">
                <label for="gender"
                  >AF2. Have you been on therapy for your atrial fibrillation for 6 months or more?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="atrial_therapy"
                    v-model="atrial_trail"
                    @change="toggleRadio('atrial_therapy', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="atrial_therapy"
                    v-model="atrial_therapy"
                    @change="toggleRadio('atrial_therapy', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div v-show="atrial" class="form-group">
                <label for="gender"
                  >AF3. Has your atrial fibrillation been well controlled with treatment for 6 months or more?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="atrial_controlled"
                    v-model="atrial_controlled"
                    @change="toggleRadio('atrial_controlled', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="atrial_controlled"
                    v-model="atrial_controlled"
                    @change="toggleRadio('atrial_controlled', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
            
              <div class="form-group">
                <label for="gender"
                  >BPH1. Do you have Benign Prostatic Hyperplasia (BPH)?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="bph"
                    v-model="bph"
                    @change="toggleRadio('bph', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="bph"
                    v-model="bph"
                    @change="toggleRadio('bph', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div v-show="bph" class="form-group">
                <label for="gender"
                  >BPH2. Are you on stable treatment for BPH?</label
                >

                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="bph_stable"
                    v-model="bph_stable"
                    @change="toggleRadio('bph_stable', true)"
                    :value="true"
                  />
                  <label class="form-check-label" for="Male"> Yes </label>
                </div>
                <div class="form-check col-md-4">
                  <input
                    class="form-check-input"
                    type="radio"
                    id="bph_stable"
                    v-model="bph_stable"
                    @change="toggleRadio('bph_stable', false)"
                    :value="false"
                  />
                  <label class="form-check-label" for="Female"> No </label>
                </div>
              </div>
              <div class="form-group">
                <label for="dropdown">Where did you hear about us?</label>
                <select id="dropdown" v-model="info" class="form-control">
                  <option selected>Choose...</option>
                  <option value="AL">Facebook</option>
                  <option value="AK">Instagram</option>
                  <option value="AZ">Email</option>
                  <option value="AR">Flyers</option>
                  <option value="CA">Craigslist</option>
                  <option value="CA">Referral</option>
                  <option value="CA">Other</option>
                </select>
              </div>
              <div class="form-group">
                <label for="text">Please specify 'Other'</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="info_other"
                  id="number"
                />
              </div>
              <div class="form-group">
                <label for="text">Any other comments</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="other_comments"
                  id="number"
                />
              </div>

              <div class="form-group">
                <div class="col-md-4">
                  <button
                    type="button"
                    @click="submit()"
                    class="btn btn-primary"
                  >
                    Submit
                  </button>
                </div>
              </div>
              <!-- End input fields -->
              <p class="copyright">
                &copy; Bootstrap 4 Survey Form by
                <a href="https://github.com/sharat005">Sharat</a>.
              </p>
            </form>
            <!-- Form end -->
          </div>
        </div>
      </div>
    </body>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
  name: "Screen",
  props: ['email','zipcode'],
  data() {
    return {
        eligible: true,
        smoked: '',
        copd: '',
        diabetes: '',
        copd_flare: '',
        bp_medicine: '',
        pregnant: false,
        asthma: '',
        lung_disease: '',
        lung_cancer: false,
        glaucome: '',
        clinical_trial: '',
        antibiotics: '',
        atrial: '',
        atrial_therapy: '',
        atrial_controlled: true,
        bph: '',
        bph_stable: true,
        smoking_start_age: null,
        smoking_stop_age: null,
        bp_medicine_list: '',
        smoke_count: null,
        ashthma_age: null,
        lung_disease_desc: '',
        info: '',
        info_other: '',
        other_comments: '',
        clinical_trail: '',
      }
  },
  created() {
    console.log('prop email-----', this.email);
  },
  computed: {
    packYears() {
      return this.smoke_count * (this.smoking_stop_age - this.smoking_start_age)
    }
  },
  methods: {
    isEligible() {
      console.log('iseligible block of code-----', !this.smoked, this.diabetes, this.lung_cancer, this.atrial_therapy, this.glaucome, !this.bph_stable)
      if(!this.smoked || this.diabetes || this.lung_cancer || this.atrial_therapy || this.glaucome || !this.bph_stable) {
        this.eligible = false;
      }
    },
    changeRadio() {
      console.log('copd var changed123', this.copd);
    },
    toggleRadio(attr, val) {
      console.log("val comes in toggleRadio123----", val);
      this[attr] = val;
    },
    // axios backend call to post the information filled in Page 1
    async submit() {
      console.log(
        "user object before sending-----",
        this.smoked, this.copd, this.copd_flare
      );
      await axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/record/records/",
        data: {
          // Send description and status to the server
            smoked: this.smoked,
            copd: this.copd,
            copd_flare: this.copd_flare,
            bp_medicine: this.bp_medicine,
            pregnant: this.pregnant,
            asthma: this.asthma,
            diabetes: this.diabetes,
            lung_disease: this.lung_disease,
            lung_cancer: this.lung_cancer,
            glaucome: this.glaucome,
            clinical_trial: this.clinical_trial,
            atrial: this.atrial,
            atrial_therapy: this.atrial_therapy,
            atrial_controlled: this.atrial_controlled,
            antibiotics: this.antibiotics,
            bph: this.bph,
            bph_stable: this.bph_stable,
            smoking_start_age: this.smoking_start_age,
            smoking_stop_age: this.smoking_stop_age,
            bp_medicine_list: this.bp_medicine_list,
            smoke_count: this.smoke_count,
            ashthma_age: this.ashthma_age,
            lung_disease_desc: this.lung_disease_desc,
            info: this.info,
            info_other: this.info_other,
            other_comments: this.other_comments,
            clinical_trail: this.clinical_trail,
        },
        auth: {
          // Basic authentication
          username: "sharatnaik",
          password: "12345678",
        },
      })
        .then((response) => {
          console.log("Response from the POST Method", response);
          // let newTask = {'id': response.data.id, 'description': this.description, 'status': this.status}

          // this.tasks.push(newTask)

          // this.description = '' // Reset description
          // this.status = 'todo' // Reset status
        })
        .catch((error) => {
          console.log(error);
        });
      this.isEligible();
      // router.push({ path: "/eligibility" });
      router.push({ name: 'Eligibility', params: { eligible: this.eligible, zipcode: this.zipcode } })

    },
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
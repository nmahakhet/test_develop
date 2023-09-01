<template>
  <div class="bg-[#ededed]">
    <div class="p-10">
      <div class="flex flex-row mb-10">
        <v-btn color="orange-darken-2" @click="back">
          <v-icon start icon="mdi-arrow-left"></v-icon>
          Back
        </v-btn>
      </div>
      <div class="bg-white p-5">
        <div class="flex flex-row">
          <h3>Line Number: {{ formInfoData.line_number }}</h3>
        </div>
        <div class="border-b-2 border-blue-500 text-center pb-2 mb-4 font-bold">
          CML
        </div>
        <v-divider class="border-opacity-50" color="info"></v-divider>
        <div class="flex flex-row flex-row-reverse mb-5">
          <v-btn @click="onCreateCml"
            ><v-icon start icon="mdi-plus-circle"></v-icon>Add CML</v-btn
          >
        </div>
        <v-table class="border-collapse">
          <thead>
            <tr>
              <th
                v-for="(header, index) in headers"
                :key="index"
                class="header-cell text-center text-white"
              >
                {{ header }}
              </th>
              <th class="header-cell text-center text-white"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data, index) in cmlDatas" :key="index">
              <td class="body-cell">{{ data.cml_number }}</td>
              <td class="body-cell">{{ data.cml_description }}</td>
              <td class="body-cell">{{ actualOutsideDiameter }}</td>
              <td class="body-cell">{{ designThickness }}</td>
              <td class="body-cell">{{ structuralThickness }}</td>
              <td class="body-cell">{{ requiredThickness }}</td>
              <td class="body-cell actions">
                <span @click="onEditCml(data.id)"
                  ><v-icon start icon="mdi-pencil-circle"></v-icon
                ></span>
                <span @click="onDeleteCml(data.id)">
                  <v-icon start icon="mdi-delete-circle"></v-icon>
                </span>
              </td>
            </tr>
          </tbody>
        </v-table>
      </div>
      <v-dialog v-model="dialog" width="800">
        <v-card>
          <v-card-title>
            <span class="text-h5">Info</span>
          </v-card-title>
          <v-card-text>
            <form @submit.prevent="submit">
              <template v-if="typeDialog === 'create'">
                <v-text-field
                  v-model="createData.cml_number"
                  :label="formatLabel('cml_number')"
                ></v-text-field>
                <v-text-field
                  v-model="createData.cml_description"
                  :label="formatLabel('cml_description')"
                ></v-text-field>
                <v-text-field
                  v-model="designThickness"
                  :label="formatLabel('design_thickness')"
                  :disabled="true"
                ></v-text-field>
                <v-text-field
                  v-model="structuralThickness"
                  :label="formatLabel('structural_thickness')"
                ></v-text-field>
                <v-text-field
                  v-model="actualOutsideDiameter"
                  :label="formatLabel('actual_outside_diameter')"
                ></v-text-field>
                <v-text-field
                  v-model="requiredThickness"
                  :label="formatLabel('required_thickness')"
                  :disabled="true"
                ></v-text-field>
              </template>
              <template v-else>
                <v-text-field
                  v-model="editData.cml_number"
                  :label="formatLabel('cml_number')"
                ></v-text-field>
                <v-text-field
                  v-model="editData.cml_description"
                  :label="formatLabel('cml_description')"
                ></v-text-field>
                <v-text-field
                  v-model="designThickness"
                  :label="formatLabel('design_thickness')"
                  :disabled="true"
                ></v-text-field>
                <v-text-field
                  v-model="structuralThickness"
                  :label="formatLabel('structural_thickness')"
                  :disabled="true"
                ></v-text-field>
                <v-text-field
                  v-model="actualOutsideDiameter"
                  :label="formatLabel('actual_outside_diameter')"
                  :disabled="true"
                ></v-text-field>
                <v-text-field
                  v-model="requiredThickness"
                  :label="formatLabel('required_thickness')"
                  :disabled="true"
                ></v-text-field>
              </template>

              <v-btn color="green-darken-1" class="me-4" type="submit">
                submit
              </v-btn>
            </form>
          </v-card-text>
        </v-card>
      </v-dialog>
      <div class="bg-white p-5 mt-3">
        <div
          class="border-b-2 border-blue-500 text-center pb-2 mb-4 mt-20 font-bold"
        >
          Test Point
        </div>
        <v-select
          label="Select"
          :items="options"
          variant="outlined"
          item-value="value"
          item-title="text"
          v-model="selectCmlId"
        ></v-select>
        <template v-if="selectCmlId">
          <TestPointComponent :id="selectCmlId" />
        </template>
      </div>
      <div class="bg-white p-5 mt-3">
        <div
          class="border-b-2 border-blue-500 text-center pb-2 mb-4 mt-20 font-bold"
        >
          Thickness
        </div>
        <v-select
          label="Select"
          :items="optionsThickness"
          variant="outlined"
          item-value="value"
          item-title="text"
          v-model="selectTestPointId"
        ></v-select>
        <template v-if="selectTestPointId">
          <ThicknessComponent :id="selectTestPointId" />
        </template>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { getCml, createCml, updateCml, deleteCml } from "@/api/pipingApi";
import { useStore } from "vuex";
import TestPointComponent from "../components/TestPoint.vue";
import ThicknessComponent from "../components/Thickness.vue";

export default defineComponent({
  name: "DetailsView",
  components: { TestPointComponent, ThicknessComponent },
  props: {
    id: {
      type: String,
      default: "1",
    },
  },
  data() {
    const headers: Array<string> = [
      "CML Number",
      "CML Description",
      "Actual Outside Diameter",
      "Design Thickness(mm)",
      "Structural Thickness(mm)",
      "Required Thickness(mm)",
    ];
    const cmlDatas: Array<any> = [];
    const templateCmlData = {
      cml_number: 0,
      cml_description: 0,
      design_thickness: 0,
      structural_thickness: 0,
      actual_outside_diameter: 0,
      required_thickness: 0,
    };
    const editData = templateCmlData;
    const createData = templateCmlData;
    return {
      headers,
      cmlDatas,
      dialog: false,
      editData,
      createData,
      templateCmlData,
      idActive: 1,
      idInfo: "1",
      selectCmlId: 0,
      typeDialog: "create",
      searchQuery: "",
      selectTestPointId: 0,
      propertyNames: [
        "cml_number",
        "cml_description",
        "design_thickness",
        "structural_thickness",
        "actual_outside_diameter",
        "required_thickness",
      ],
    };
  },
  async created() {
    const res = await getCml(this.id);
    this.idInfo = this.id;
    this.cmlDatas = res;
  },
  computed: {
    formInfoData() {
      return useStore().state.formInfoData;
    },
    actualOutsideDiameter() {
      return this.pipeSizeToOutsideDiameter(this.formInfoData.pipe_size);
    },
    structuralThickness() {
      return this.calculateStructuralThickness(this.formInfoData.pipe_size);
    },
    designThickness() {
      return this.calculateDesignPressure(
        Number(this.formInfoData.design_pressure),
        Number(this.actualOutsideDiameter),
        Number(this.formInfoData.stress),
        Number(this.formInfoData.joint_efficiency)
      );
    },
    requiredThickness() {
      return Math.max(
        Number(this.designThickness),
        Number(this.structuralThickness)
      );
    },
    options() {
      const def = {
        value: 0,
        text: "Select CML Number",
      };
      return this.cmlDatas
        .map((val: any) => {
          const structure = {
            value: val.id,
            text: val.cml_number,
          };
          return structure;
        })
        .concat(def);
    },
    optionsThickness() {
      const def = {
        value: 0,
        text: "Select Testpoint Number",
      };
      if (!useStore().state.testpointData) return def;
      console.log(useStore().state.testpointData);
      return useStore()
        .state.testpointData.map((val: any) => {
          const structure = {
            value: val.id,
            text: val.tp_number,
          };
          return structure;
        })
        .concat(def);
    },
  },
  methods: {
    back() {
      this.$router.push({ name: "piping" });
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    onCreateCml() {
      this.typeDialog = "create";
      this.createData = this.templateCmlData;
      this.dialog = true;
    },
    async onEditCml(id: number) {
      this.typeDialog = "edit";
      const data = this.cmlDatas.find((val) => val.id === id);
      this.editData = JSON.parse(JSON.stringify(data));
      this.idActive = id;
      this.dialog = true;
    },
    formatLabel(property: string) {
      // Replace underscores with spaces and capitalize the property name
      return property.replace(/_/g, " ").toUpperCase();
    },
    async submit() {
      if (this.typeDialog === "create") {
        const structure = {
          cml_number: this.createData.cml_number,
          cml_description: this.createData.cml_description,
          design_thickness: this.designThickness,
          structural_thickness: this.structuralThickness,
          actual_outside_diameter: this.actualOutsideDiameter,
          required_thickness: this.requiredThickness,
          info_id: this.idInfo,
        };
        await createCml(structure);
      } else {
        const structure = {
          cml_number: this.editData.cml_number,
          cml_description: this.editData.cml_description,
          design_thickness: this.designThickness,
          structural_thickness: this.structuralThickness,
          actual_outside_diameter: this.actualOutsideDiameter,
          required_thickness: this.requiredThickness,
          info_id: this.idInfo,
        };
        await updateCml(this.idActive, structure);
      }

      const res = await getCml(this.idInfo.toString());
      this.cmlDatas = res;
      alert("Success");
      this.dialog = false;
      return;
    },
    calculateStructuralThickness(pipeSizeInches: string) {
      const pipeSize = parseFloat(pipeSizeInches);

      if (pipeSize <= 2) {
        return 1.8;
      } else if (pipeSize === 3) {
        return 2.0;
      } else if (pipeSize === 4) {
        return 2.3;
      } else if (pipeSize >= 6 && pipeSize <= 18) {
        return 2.8;
      } else if (pipeSize >= 20) {
        return 3.1;
      } else {
        return null;
      }
    },
    calculateDesignPressure(
      designPressure: number,
      actualOutsideDiameter: number,
      stress: number,
      jointEfficiency: number
    ) {
      const numerator = designPressure * actualOutsideDiameter;
      const denominator =
        2 * stress * jointEfficiency + 2 * designPressure * 0.4;

      if (denominator === 0) {
        throw new Error("Denominator cannot be zero. Check input values.");
      }

      return (numerator / denominator).toFixed(2);
    },
    pipeSizeToOutsideDiameter(pipeSizeInches: string): number | null {
      const formattedPipeSize = parseFloat(pipeSizeInches).toFixed(3);
      const pipeSizeData: Record<string, number> = {
        "0.125": 10.3,
        "0.250": 13.7,
        "0.357": 17.1,
        "0.500": 21.3,
        "0.750": 26.7,
        "1.000": 33.4,
        "1.250": 42.2,
        "1.500": 48.3,
        "2.000": 60.3,
        "2.500": 73.0,
        "3.000": 88.9,
        "3.500": 101.6,
        "4.000": 114.3,
        "5.000": 141.3,
        "6.000": 168.3,
        "8.000": 219.1,
        "10.000": 273.0,
        "12.000": 323.8,
        "14.000": 355.6,
        "16.000": 406.4,
        "18.000": 457.0,
        // Add more mappings as needed
      };
      if (Reflect.has(pipeSizeData, formattedPipeSize)) {
        return pipeSizeData[formattedPipeSize];
      } else {
        // Handle the case where the input pipe size is not found in the mapping.
        return null;
      }
    },
    async onDeleteCml(id: any) {
      await deleteCml(id);
      alert("Success");
      const res = await getCml(this.idInfo);
      this.cmlDatas = res;
    },
  },
});
</script>
<style scoped>
.border-collapse {
  border-collapse: collapse;
  width: 100%; /* Ensure table width spans the container */
}

.header-cell {
  background-color: #3490dc; /* Header cell background color */
  color: #ffffff; /* Header cell text color */
  padding: 0.5rem;
  text-align: center; /* Center-align text in header cells */
}

.body-row:hover {
  background-color: #e2e8f0; /* Body row background color on hover */
}

.body-cell {
  padding: 0.5rem;
}

.actions span {
  cursor: pointer;
  color: #3490dc; /* Action link color */
  margin-right: 1rem;
}

.actions span:hover {
  text-decoration: underline; /* Underline the action link on hover */
  color: #2779bd; /* Hovered action link color */
}
</style>

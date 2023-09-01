<template>
  <div class="bg-[#ededed]">
    <div class="p-10">
      <div class="bg-white p-5">
        <v-date-picker locale="en"></v-date-picker>
        <div class="flex flex-row flex-row-reverse mb-5">
          <v-btn @click="onCreateLineNumber"
            ><v-icon start icon="mdi-plus-circle"></v-icon>Add Line
            Number</v-btn
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
            <tr
              v-for="(data, index) in infoDatas"
              :key="index"
              class="body-row"
            >
              <td class="body-cell">{{ data.line_number }}</td>
              <td class="body-cell">{{ data.location }}</td>
              <td class="body-cell">{{ data.from_location }}</td>
              <td class="body-cell">{{ data.to_location }}</td>
              <td class="body-cell">{{ data.pipe_size }}</td>
              <td class="body-cell">{{ data.service }}</td>
              <td class="body-cell">{{ data.material }}</td>
              <td class="body-cell actions">
                <span @click="handlerEditInfo(data.id)"
                  ><v-icon start icon="mdi-pencil-circle"></v-icon
                ></span>
                <span @click="handlerDetails(data.id)"
                  ><v-icon start icon="mdi-eye-outline"></v-icon
                ></span>
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
              <template v-for="property in propertyNames" :key="property">
                <v-text-field
                  v-if="typeDialog === 'edit'"
                  v-model="filterData[property]"
                  :label="formatLabel(property)"
                ></v-text-field>
                <v-text-field
                  v-else
                  v-model="createData[property]"
                  :label="formatLabel(property)"
                ></v-text-field>
              </template>

              <v-btn color="green-darken-1" class="me-4" type="submit">
                submit
              </v-btn>
            </form>
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import { useStore } from "vuex";
import { mapActions } from "vuex";
import { createInfo } from "@/api/pipingApi";

export default defineComponent({
  name: "PipingView",
  data() {
    const now = new Date();

    // Format the date as 'YYYY-MM-DD' (or any desired format)
    const formattedDate = `${now.getFullYear()}-${(now.getMonth() + 1)
      .toString()
      .padStart(2, "0")}-${now.getDate().toString().padStart(2, "0")}`;
    const headers: Array<string> = [
      "line_number",
      "location",
      "from",
      "to",
      "Pipe size(inch)",
      "service",
      "material",
    ];
    const templateInfoData = {
      ca: 0,
      design_life: 0,
      design_pressure: 0,
      design_temperature: 0,
      drawing_number: 0,
      from_location: 0,
      inservice_date: formattedDate,
      joint_efficiency: 0,
      line_number: 0,
      location: 0,
      material: 0,
      operating_pressure: 0,
      operating_temperature: 0,
      original_thickness: 0,
      pipe_size: 0,
      service: 0,
      stress: 0,
      to_location: 0,
    };
    const filterData = templateInfoData;
    const createData = templateInfoData;
    // const headers: Array<string> = [
    //   "ca",
    //   "design_life",
    //   "design_pressure",
    //   "design_temperature",
    //   "drawing_number",
    //   "from_location",
    //   "inservice_date",
    //   "joint_efficiency",
    //   "line_number",
    //   "location",
    //   "material",
    //   "operating_pressure",
    //   "operating_temperature",
    //   "original_thickness",
    //   "pipe_size",
    //   "service",
    //   "stress",
    //   "to_location",
    // ];

    return {
      headers,
      dialog: false,
      filterData,
      idActive: 1,
      typeDialog: "edit",
      createData,
      templateInfoData,
      selectedDate: "2023-09-01",
      propertyNames: [
        "ca",
        "design_life",
        "design_pressure",
        "design_temperature",
        "drawing_number",
        "from_location",
        "inservice_date",
        "joint_efficiency",
        "line_number",
        "location",
        "material",
        "operating_pressure",
        "operating_temperature",
        "original_thickness",
        "pipe_size",
        "service",
        "stress",
        "to_location",
      ],
      searchQuery: "",
    };
  },
  async created() {
    await this.fetchInfoData();
  },
  computed: {
    infoDatas() {
      return useStore().state.infoDatas;
    },
    formInfoData() {
      return useStore().state.formInfoData;
    },
  },
  methods: {
    ...mapActions([
      "fetchInfoData",
      "setFormInfoDatas",
      "setInfoDatas",
      "updateInfo",
    ]),
    handlerDetails(id: number) {
      const filteredData = this.infoDatas.find((val: any) => val.id === id);
      this.setFormInfoDatas(filteredData);
      this.$router.push({ name: "DetailsView", params: { id } });
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    handlerEditInfo(id: number) {
      this.idActive = id;
      this.typeDialog = "edit";
      const filteredData = this.infoDatas.find((val: any) => val.id === id);
      this.filterData = JSON.parse(JSON.stringify(filteredData));
      this.dialog = true;
    },
    onCreateLineNumber() {
      this.typeDialog = "create";
      this.createData = this.templateInfoData;
      this.dialog = true;
    },
    async submit() {
      if (this.typeDialog === "create") {
        await createInfo(this.createData);
        await this.fetchInfoData();
        this.dialog = false;
        return;
      }
      let infoAll = this.infoDatas;
      const newInfo = infoAll.map((val: any) => {
        if (val.id === this.idActive) return this.filterData;
        return val;
      });
      await this.updateInfo({ id: this.idActive, data: this.filterData });
      await this.fetchInfoData();
      alert("Success");
      this.dialog = false;
      return;
    },
    formatLabel(property: string) {
      // Replace underscores with spaces and capitalize the property name
      return property.replace(/_/g, " ").toUpperCase();
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

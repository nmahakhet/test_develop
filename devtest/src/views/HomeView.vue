<template>
  <div class="home">
    <v-table>
      <thead>
        <tr>
          <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in infoDatas" :key="index">
          <td>{{ data.line_number }}</td>
          <td>{{ data.location }}</td>
          <td>{{ data.from_location }}</td>
          <td>{{ data.to_location }}</td>
          <td>{{ data.pipe_size }}</td>
          <td>{{ data.service }}</td>
          <td>{{ data.material }}</td>
          <td><span>detail</span></td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "HomeView",
  data() {
    const headers: Array<string> = [
      "line_number",
      "location",
      "from",
      "to",
      "Pipe size(inch)",
      "service",
      "material",
    ];
    const infoDatas: Array<any> = [];
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
      infoDatas,
    };
  },
});
</script>

<template>
  <v-container
    id="regular-tables-view"
    fluid
    tag="section"
  >
    <v-card
        class="mx-auto"
        elevation="4"
    >
        <v-card-title font-color="primary" class="text-h3">Survey Management</v-card-title>
        <v-sparkline
            :value="value"
            :gradient="gradient"
            :smooth="radius || false"
            :padding="padding"
            :line-width="width"
            :stroke-linecap="lineCap"
            :gradient-direction="gradientDirection"
            :fill="fill"
            :type="type"
            :auto-line-width="autoLineWidth"
            :labels="labels"
            auto-draw
        >
        <!-- <template v-slot:label="item">
            {{ item.value }}
          </template> -->
        </v-sparkline>
        <!-- <v-card-text class="text--primary">
        <div>To send out the survey, click 'Send Survey'</div>
        <div>To view the analysis report, click 'View Report'</div>
        </v-card-text> -->
        <v-card-actions>
        <v-btn
        color="primary"
        min-width="150"
        class="mr-5"
        >
            Send Surveys
        </v-btn>
        <v-btn
        color="info"
        min-width="150"
        >
            View Report
        </v-btn>
        </v-card-actions>
    </v-card>

    <div class="py-3" />

    <material-card
      icon="mdi-clipboard-text"
      icon-small
      title="Employee Risk Level"
      color="accent"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              ID
            </th>
            <th class="primary--text">
              Name
            </th>
            <th class="primary--text">
              Country
            </th>
            <th class="primary--text">
              City
            </th>
            <th class="text-right primary--text">
              Risk
            </th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>1</td>
            <td>Dakota Rice</td>
            <td>Singapore</td>
            <td>Singapore</td>
            <td class="text-right">
              98%
            </td>
          </tr>

          <tr>
            <td>2</td>
            <td>Minverva Hooper</td>
            <td>Curaçao</td>
            <td>Sinaas-Waas</td>
            <td class="text-right">
              94%
            </td>
          </tr>

          <tr>
            <td>3</td>
            <td>Sage Rodriguez</td>
            <td>Netherlands</td>
            <td>Baileux</td>
            <td class="text-right">
              88%
            </td>
          </tr>

          <tr>
            <td>4</td>
            <td>Philip Chaney</td>
            <td>Korea, South</td>
            <td>Overland Park</td>
            <td class="text-right">
              79%
            </td>
          </tr>

          <tr>
            <td>5</td>
            <td>Doris Greene</td>
            <td>Malawi</td>
            <td>Feldkirchen in Kärnten</td>
            <td class="text-right">
              65%
            </td>
          </tr>

          <tr>
            <td>6</td>
            <td>Mason Porter</td>
            <td>Chile</td>
            <td>Gloucester</td>
            <td class="text-right">
              57%
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </material-card>

    <div class="py-3" />

    <material-card
      dark
      icon="mdi-clipboard-plus"
      icon-small
      title="Surveys Yet Completed"
      color="accent"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Country</th>
            <th>City</th>
            <th class="text-right">
              Contact
            </th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>1</td>
            <td>Dakota Rice</td>
            <td>Niger</td>
            <td>Oud-Turnhout</td>
            <td class="text-right">
              Dakota_Rice@samplemail.com
            </td>
          </tr>

          <tr>
            <td>2</td>
            <td>Minverva Hooper</td>
            <td>Curaçao</td>
            <td>Sinaas-Waas</td>
            <td class="text-right">
              Minverva_Hooper@samplemail.com
            </td>
          </tr>

          <tr>
            <td>3</td>
            <td>Sage Rodriguez</td>
            <td>Netherlands</td>
            <td>Baileux</td>
            <td class="text-right">
              Sage_Rodriguez@samplemail.com
            </td>
          </tr>

          <tr>
            <td>4</td>
            <td>Philip Chaney</td>
            <td>Korea, South</td>
            <td>Overland Park</td>
            <td class="text-right">
              Philip_Chaney@samplemail.com
            </td>
          </tr>

          <tr>
            <td>5</td>
            <td>Doris Greene</td>
            <td>Malawi</td>
            <td>Feldkirchen in Kärnten</td>
            <td class="text-right">
              Doris_Greene@samplemail.com
            </td>
          </tr>

          <tr>
            <td>6</td>
            <td>Mason Porter</td>
            <td>Chile</td>
            <td>Gloucester</td>
            <td class="text-right">
              Mason_Porter@samplemail.com
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </material-card>
  </v-container>
</template>

<script>
    import ApexCharts from 'apexcharts'
    const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
    ]
  export default {
    name: 'RegularTablesView',
    data:() => ({
        width: 2,
        radius: 10,
        padding: 10,
        lineCap: 'round',
        gradient: gradients[5],
        value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8],
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        gradientDirection: 'top',
        gradients,
        fill: false,
        type: 'trend',
        autoLineWidth: false,
        series: [44, 55, 41, 17, 15],
        chartOptions: {
          chart: {
            type: 'donut',
          },
          responsive: [{
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                position: 'bottom'
              }
            }
          }]
        },
    })
  }
  
</script>

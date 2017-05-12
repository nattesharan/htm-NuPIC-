#define the model of the dataset
SWARM_DESCRIPTION = {
  "includedFields": [ #information regarding the fields
    {
      "fieldName": "timestamp",
      "fieldType": "datetime"
    },
    {
      "fieldName": "kw_energy_consumption",
      "fieldType": "float",
      "maxValue": 53.0,
      "minValue": 0.0
    }
  ],
  "streamDef": { #infomation about the prediction
    "info": "kw_energy_consumption",
    "version": 1,
    "streams": [
      {
        "info": "Rec Center",
        "source": "file://rec-center-hourly.csv",#source file i.e csv file
        "columns": [
          "*" #all the columns
        ]
      }
    ]
  },

  "inferenceType": "TemporalMultiStep",#type of prediction
  "inferenceArgs": {
    "predictionSteps": [#how many steps of future we want to predict
      1
    ],
    "predictedField": "kw_energy_consumption"#field which is to be predicted
  },
  "iterationCount": 1,#1 indicates all rows -1 indicates 1 row
  "swarmSize": "medium"#small is for debugging medium is fine large takes a lot of time
}

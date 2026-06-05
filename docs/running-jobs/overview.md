# How do I use CURC resources? 

The purpose of this page is to give a general introduction to submitting Slurm jobs on CURC resources. 

Get a CURC account. 


## What are the different ways to submit a job? 

Below we give a very brief summary of the different ways to submit a job ...

1. GUI based
    - Open OnDemand 
        - By far the easiest way to submit a job to CURC resources
        - Can do batch jobs and gives access to a terminal 
        - Applications are limited
            - Bad for long running jobs 
2. Command line based
    - Starting an interactive job that puts you on a compute node where you can use the command line 
        - Enables the user to interactivity run jobs from the command line 
        - Can enable you to run interactive GUI applications 
        - Great for troubleshooting, testing, and compiling code
        - Can be done through `sinteractive`, `acompile`
        - Should not be used when requesting a large amount of resources. The resources need to become available before you can use them. 
    - Submitting a batch job
        - No interactivity 
        - Fantastic for long running jobs. Allows you to submit items to the system and have them run at a later time.
        - Allows you to scale up your work
        - The preferred approach on HPC systems, when possible 


For all of the above ways to submit a job, it is very important to understand how you get access to resources on CURC resources 

```{important}
You should be on a login node when you submit jobs via the command line. It is not necessary to be on a compute node, unless your workflow requires computational resources to submit a job.
```

## Clusters 

CURC has two HPC clusters: Alpine and Blanca. For individuals with a CURC account, Alpine is a freely available resource. Blanca is a "condo" compute cluster, which in short means that nodes must be purchased before a user can utilize Blanca resources or they must be given permission to run on Blanca resources by an individual who owns Blanca resources. 

To submit jobs to each cluster you must specify the correct Cluster in Open OnDemand custom configurations or if you are running jobs from the command line, you must be sure to load the appropriate Slurm modules:

```{tip}
For more information on modules see ... 
```

(tabset-ref-slurm-mods)=
`````{tab-set}
:sync-group: tabset-slurm-mods

````{tab-item} Alpine
:sync: slurm-mods-alpine

When you get onto a login node, the `slurm/alpine` module is loaded by default. You do not need to load this module, unless you are switching between the Alpine and Blanca clusters. 

```bash
module load slurm/alpine
```

````

```` {tab-item} Blanca
:sync: slurm-mods-blanca

Before submitting jobs from a login node, you must load the Blanca Slurm module to get access to Blanca resources: 

```bash
module load slurm/blanca
```

````
`````

## Slurm directives

To submit a job to specific resources, users must utilize Slurm directives. Slurm directives can be utilized by all job submission options, however, they are essential if a user is going to submit a command line interactive job or job script.

In this section, we provide the standard Slurm directives that should be considered for any job submitted to CURC resources. 

```{tip}
Do you want to have finer control of the resources you are requesting? Then see Slurms documentation on all possible Slurm directives https://slurm.schedmd.com/sbatch.html#SECTION_OPTIONS
```

### Account

`--account`


### Partition 

`--partition`

Partition is how we group together different hardware types on Alpine. On Blanca, we utilize partitions as a way to specify nodes belonging to a particular group. 

Link to appropriate resources for Blanca and Alpine 

### Quality of Service (QoS)

`--qos`

On Alpine we utilize the QoS in several different ways. The two primary ways we utilize the QoS are to 
1. Separate resources available for 24 hour or less jobs and jobs that are longer than 24 hours and less than or equal to 7 days
2. Provide access to testing resources 

On Blanca each group has their own QoS that can be modified to fit their needs. Additionally, all Blanca users have access to the `preemptable` QoS, which can be used to submit preemptable jobs

Link to appropriate resources for Blanca and Alpine 


### Gres 

`--gres`

On both Alpine and Blanca Gres is used to access GPU resources. GPU resources are only available on particular nodes. 

Link to appropriate resources for Blanca and Alpine 

### ntasks

`--ntasks`


### Number of Compute Nodes

`--nodes`

### Wall time

`--time`

### Additional resources flags

Table of remaining ones from running-jobs/job-resources.html#partitions


## Submitting a job 

## Monitoring a job 

- useful slurm commands section 
- squeue Status and Reason codes 
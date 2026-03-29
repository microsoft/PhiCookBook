# Профињшавање и интеграција прилагођених Phi-3 модела са Prompt flow у Microsoft Foundry

Овај пример од почетка до краја (E2E) заснован је на водичу "[Профињшавање и интеграција прилагођених Phi-3 модела са Prompt Flow у Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community. Уводи вас у процесе профињшавања, распореда и интеграције прилагођених Phi-3 модела са Prompt flow у Microsoft Foundry.
За разлику од E2E примера, "[Профињшавање и интеграција прилагођених Phi-3 модела са Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", који је укључивао покретање кода локално, овај туторијал се у потпуности фокусира на профињшавање и интеграцију вашег модела унутар Azure AI / ML Studio.

## Преглед

У овом E2E примеру научићете како да профињшате Phi-3 модел и интегришете га са Prompt flow у Microsoft Foundry. Користећи Azure AI / ML Studio, успоставићете радни ток за распоредање и коришћење прилагођених AI модела. Овај E2E пример је подељен у три сценарија:

**Сценарио 1: Постављање Azure ресурса и припрема за профињшавање**

**Сценарио 2: Профињшавање Phi-3 модела и распоређивање у Azure Machine Learning Studio**

**Сценарио 3: Интеграција са Prompt flow и разговор са вашим прилагођеним моделом у Microsoft Foundry**

Ево прегледа овог E2E примера.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/sr/00-01-architecture.198ba0f1ae6d841a.webp)

### Садржај

1. **[Сценарио 1: Постављање Azure ресурса и припрема за профињшавање](#сценарио-1-постављање-azure-ресурса-и-припрема-за-профињшавање)**
    - [Креирање Azure Machine Learning радног простора](#креирање-azure-machine-learning-радног-простора)
    - [Захтев за GPU квоте у Azure претплати](#захтев-за-gpu-квоте-у-azure-претплати)
    - [Додавање доделе улоге](#додавање-доделе-улоге)
    - [Постављање пројекта](#постављање-пројекта)
    - [Припрема скупa података за профињшавање](#припремите-скуп-података-за-фино-подешавање)

1. **[Сценарио 2: Профињшавање Phi-3 модела и распоређивање у Azure Machine Learning Studio](#сценарио-2-фино-подешавање-phi-3-модела-и-распоређивање-у-azure-machine-learning-studio)**
    - [Профињшавање Phi-3 модела](#фино-подесите-phi-3-модел)
    - [Распоређивање профињшаног Phi-3 модела](#распоредите-фино-подешени-phi-3-модел)

1. **[Сценарио 3: Интеграција са Prompt flow и разговор са вашим прилагођеним моделом у Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Интеграција прилагођеног Phi-3 модела са Prompt flow](#интегришите-прилагођени-phi-3-модел-са-prompt-flow)
    - [Разговор са вашим прилагођеним Phi-3 моделом](#разговарајте-са-својим-прилагођеним-phi-3-моделом)

## Сценарио 1: Постављање Azure ресурса и припрема за профињшавање

### Креирање Azure Machine Learning радног простора

1. Укуцајте *azure machine learning* у **претраживачку траку** на врху странице портала и изаберите **Azure Machine Learning** из понуђених опција.

    ![Type azure machine learning.](../../../../../../translated_images/sr/01-01-type-azml.acae6c5455e67b4b.webp)

2. Изаберите **+ Create** из навигационог менија.

3. Изаберите **New workspace** из навигационог менија.

    ![Select new workspace.](../../../../../../translated_images/sr/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Извршите следеће задатке:

    - Изаберите вашу Azure **Subscription**.
    - Изаберите **Resource group** коју ћете користити (или креирајте нову ако је потребно).
    - Унесите **Workspace Name**. Мора бити јединствена вредност.
    - Изаберите **Region** коју желите да користите.
    - Изаберите **Storage account** који ћете користити (или креирајте нови ако је потребно).
    - Изаберите **Key vault** који ћете користити (или креирајте нови ако је потребно).
    - Изаберите **Application insights** који ћете користити (или креирајте нови ако је потребно).
    - Изаберите **Container registry** који ћете користити (или креирајте нови ако је потребно).

    ![Fill azure machine learning.](../../../../../../translated_images/sr/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Изаберите **Review + Create**.

6. Изаберите **Create**.

### Захтев за GPU квоте у Azure претплати

У овом туторијалу научићете како да профињшате и распоредите Phi-3 модел користећи GPU уређаје. За профињшавање ћете користити *Standard_NC24ads_A100_v4* GPU, за који је потребан захтев за квоту. За распоређивање ћете користити *Standard_NC6s_v3* GPU, који такође захтева захтев за квоту.

> [!NOTE]
>
> Само Pay-As-You-Go претплате (стандардни тип претплате) имају право на доделу GPU-а; претплате са повластицама тренутно нису подржане.
>

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Извршите следеће кораке да бисте затражили квоту за *Standard NCADSA100v4 Family*:

    - Изаберите **Quota** са леве стране менија.
    - Изаберите **Virtual machine family** коју желите да користите. На пример, изаберите **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, која укључује *Standard_NC24ads_A100_v4* GPU.
    - Изаберите **Request quota** из навигационог менија.

        ![Request quota.](../../../../../../translated_images/sr/02-02-request-quota.c0428239a63ffdd5.webp)

    - На страници Request quota унесите **New cores limit** који желите да користите. На пример, 24.
    - На страници Request quota изаберите **Submit** да пошаљете захтев за GPU квоту.

1. Извршите следеће кораке да бисте затражили квоту за *Standard NCSv3 Family*:

    - Изаберите **Quota** са леве стране менија.
    - Изаберите **Virtual machine family** коју желите да користите. На пример, изаберите **Standard NCSv3 Family Cluster Dedicated vCPUs**, која укључује *Standard_NC6s_v3* GPU.
    - Изаберите **Request quota** из навигационог менија.
    - На страници Request quota унесите **New cores limit** који желите да користите. На пример, 24.
    - На страници Request quota изаберите **Submit** да пошаљете захтев за GPU квоту.

### Додавање доделе улоге

Да бисте профињшали и распоредили ваше моделе, прво морате да креирате Креирану корисничку управљану идентитет (User Assigned Managed Identity - UAI) и доделите јој одговарајуће дозволе. Ова UAI биће коришћена за аутентификацију током распореда.

#### Креирање кориснички додељене управљане идентитета (UAI)

1. Укуцајте *managed identities* у **претраживачку траку** на врху странице портала и изаберите **Managed Identities** из понуђених опција.

    ![Type managed identities.](../../../../../../translated_images/sr/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Изаберите **+ Create**.

    ![Select create.](../../../../../../translated_images/sr/03-02-select-create.92bf8989a5cd98f2.webp)

1. Извршите следеће задатке:

    - Изаберите вашу Azure **Subscription**.
    - Изаберите **Resource group** коју ћете користити (или креирајте нову ако је потребно).
    - Изаберите **Region** коју желите да користите.
    - Унесите **Name**. Мора бити јединствена вредност.

    ![Select create.](../../../../../../translated_images/sr/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Изаберите **Review + create**.

1. Изаберите **+ Create**.

#### Додавање улоге Contributor управљаној идентитету

1. Идите до ресурса управљане идентитета који сте креирали.

1. Изаберите **Azure role assignments** са леве стране менија.

1. Изаберите **+ Add role assignment** из навигационог менија.

1. На страници Add role assignment извршите следеће радње:
    - Изаберите **Scope** као **Resource group**.
    - Изаберите вашу Azure **Subscription**.
    - Изаберите **Resource group** који ћете користити.
    - Изаберите **Role** као **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/sr/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Изаберите **Save**.

#### Додавање улоге Storage Blob Data Reader управљаној идентитету

1. Укуцајте *storage accounts* у **претраживачку траку** на врху странице портала и изаберите **Storage accounts** из понуђених опција.

    ![Type storage accounts.](../../../../../../translated_images/sr/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Изаберите складишни налог који је повезан са Azure Machine Learning радним простором који сте креирали. На пример, *finetunephistorage*.

1. Извршите следеће кораке да бисте отишли на страницу за додавање улоге:

    - Дођите до Azure Storage налога који сте креирали.
    - Изаберите **Access Control (IAM)** са леве стране менија.
    - Изаберите **+ Add** из навигационог менија.
    - Изаберите **Add role assignment** из навигационог менија.

    ![Add role.](../../../../../../translated_images/sr/03-06-add-role.353ccbfdcf0789c2.webp)

1. На страници Add role assignment извршите следеће:

    - На страници Role укуцајте *Storage Blob Data Reader* у **претраживачку траку** и изаберите **Storage Blob Data Reader** из понуђених опција.
    - На страници Role изаберите **Next**.
    - На страници Members изаберите **Assign access to** као **Managed identity**.
    - На страници Members изаберите **+ Select members**.
    - На страници Select managed identities изаберите вашу Azure **Subscription**.
    - На страници Select managed identities изаберите **Managed identity** као **Manage Identity**.
    - На страници Select managed identities изаберите Manage Identity који сте креирали. На пример, *finetunephi-managedidentity*.
    - На страници Select managed identities изаберите **Select**.

    ![Select managed identity.](../../../../../../translated_images/sr/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Изаберите **Review + assign**.

#### Додавање улоге AcrPull управљаној идентитету

1. Укуцајте *container registries* у **претраживачку траку** на врху странице портала и изаберите **Container registries** из понуђених опција.

    ![Type container registries.](../../../../../../translated_images/sr/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Изаберите регистар контејнера који је повезан са Azure Machine Learning радним простором. На пример, *finetunephicontainerregistry*.

1. Извршите следеће кораке да бисте отишли на страницу за додавање улоге:

    - Изаберите **Access Control (IAM)** са леве стране менија.
    - Изаберите **+ Add** из навигационог менија.
    - Изаберите **Add role assignment** из навигационог менија.

1. На страници Add role assignment извршите следеће:

    - На страници Role укуцајте *AcrPull* у **претраживачку траку** и изаберите **AcrPull** из понуђених опција.
    - На страници Role изаберите **Next**.
    - На страници Members изаберите **Assign access to** као **Managed identity**.
    - На страници Members изаберите **+ Select members**.
    - На страници Select managed identities изаберите вашу Azure **Subscription**.
    - На страници Select managed identities изаберите **Managed identity** као **Manage Identity**.
    - На страници Select managed identities изаберите Manage Identity који сте креирали. На пример, *finetunephi-managedidentity*.
    - На страници Select managed identities изаберите **Select**.
    - Изаберите **Review + assign**.

### Постављање пројекта

Да бисте преузели скупове података потребне за профињшавање, подешавате локално окружење.

У овом задатку ћете

- креирати фолдер у којем ћете радити.
- креирати виртуелно окружење.
- инсталирати потребне пакете.
- креирати датотеку *download_dataset.py* за преузимање скупа података.

#### Креирање фолдера у којем ћете радити

1. Отворите терминал и укуцајте следећу команду да бисте креирали фолдер под називом *finetune-phi* у подразумеваној путањи.

    ```console
    mkdir finetune-phi
    ```

2. Укуцајте следећу команду у вашем терминалу да бисте отишли у фолдер *finetune-phi* који сте креирали.

    ```console
    cd finetune-phi
    ```

#### Креирање виртуелног окружења

1. Укуцајте следећу команду у вашем терминалу да бисте креирали виртуелно окружење под именом *.venv*.
    ```console
    python -m venv .venv
    ```

2. Укуцајте следећу команду у вашем терминалу да бисте активирали виртуелно окружење.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ако је успело, требало би да видите *(.venv)* пре подразумеваног позива команде.

#### Инсталирајте потребне пакете

1. Укуцајте следеће команде у вашем терминалу да бисте инсталирали потребне пакете.

    ```console
    pip install datasets==2.19.1
    ```

#### Креирајте `donload_dataset.py`

> [!NOTE]
> Комплетна структура фасцикле:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Отворите **Visual Studio Code**.

1. Изаберите **File** из мени траке.

1. Изаберите **Open Folder**.

1. Изаберите фасциклу *finetune-phi* коју сте креирали, која се налази на *C:\Users\yourUserName\finetune-phi*.

    ![Изаберите фасциклу коју сте креирали.](../../../../../../translated_images/sr/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. У левом панелу Visual Studio Code-а, кликните десним тастером миша и изаберите **New File** да бисте креирали нови фајл под именом *download_dataset.py*.

    ![Креирајте нови фајл.](../../../../../../translated_images/sr/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Припремите скуп података за фино подешавање

У овој вежби покренућете фајл *download_dataset.py* да бисте преузели скупове података *ultrachat_200k* у ваше локално окружење. Затим ћете користити ове скупове података за фино подешавање Phi-3 модела у Azure Machine Learning.

У овој вежби ћете:

- Додати код у фајл *download_dataset.py* за преузимање скупова података.
- Покренути фајл *download_dataset.py* да бисте преузели скупове података у ваше локално окружење.

#### Преузмите ваш скуп података коришћењем *download_dataset.py*

1. Отворите фајл *download_dataset.py* у Visual Studio Code.

1. Додајте следећи код у фајл *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Учитај скуп података са одређеним именом, конфигурацијом и односом поделе
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Подели скуп података на тренинг и тест скуп (80% тренинг, 20% тест)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Креирај директоријум ако не постоји
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Отвори фајл у режиму писања
        with open(filepath, 'w', encoding='utf-8') as f:
            # Итеријерирај кроз сваки запис у скупу података
            for record in dataset:
                # Сачувај запис као JSON објекат и упиши га у фајл
                json.dump(record, f)
                # Упиши нову линију да раздвојиш записе
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Учитај и подели ULTRACHAT_200k скуп података са специфичном конфигурацијом и односом поделе
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Извуци тренинг и тест скупове из поделе
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Сачувај тренинг скуп у JSONL фајл
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Сачувај тест скуп у посебан JSONL фајл
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Укуцајте следећу команду у вашем терминалу да бисте покренули скрипту и преузели скуп података у ваше локално окружење.

    ```console
    python download_dataset.py
    ```

1. Проверите да ли су скупови података успешно сачувани у вашу локалну фасциклу *finetune-phi/data*.

> [!NOTE]
>
> #### Напомена о величини скупа података и времену фино подешавања
>
> У овом туторијалу користите само 1% скупа података (`split='train[:1%]'`). Ово значајно смањује количину података, убрзавајући и процес отпремања и фино подешавања. Можете прилагодити проценат да бисте нашли одговарајући баланс између времена тренинга и перформанси модела. Коришћење мањег подскупа смањује време потребно за фино подешавање, чинећи процес управљивијим у оквиру туторијала.

## Сценарио 2: Фино подешавање Phi-3 модела и распоређивање у Azure Machine Learning Studio

### Фино подесите Phi-3 модел

У овој вежби ћете фино подесити Phi-3 модел у Azure Machine Learning Studio.

У овој вежби ћете:

- Креирати кластер рачунара за фино подешавање.
- Фино подесити Phi-3 модел у Azure Machine Learning Studio.

#### Креирајте кластер рачунара за фино подешавање

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изаберите **Compute** са левог менија.

1. Изаберите **Compute clusters** из навигационог менија.

1. Изаберите **+ New**.

    ![Изаберите компјутер.](../../../../../../translated_images/sr/06-01-select-compute.a29cff290b480252.webp)

1. Извршите следеће радње:

    - Изаберите регион који желите да користите.
    - Изаберите ниво виртуелне машине на **Dedicated**.
    - Изаберите тип виртуелне машине на **GPU**.
    - Филтрирајте величину виртуелне машине на **Select from all options**.
    - Изаберите величину виртуелне машине на **Standard_NC24ads_A100_v4**.

    ![Креирајте кластер.](../../../../../../translated_images/sr/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Изаберите **Next**.

1. Извршите следеће радње:

    - Унесите **Compute name**. Мора бити јединствена вредност.
    - Изаберите **Минималан број чворова** на **0**.
    - Изаберите **Максималан број чворова** на **1**.
    - Изаберите **Време неактивности пре смањења** на **120**.

    ![Креирајте кластер.](../../../../../../translated_images/sr/06-03-create-cluster.4a54ba20914f3662.webp)

1. Изаберите **Create**.

#### Фино подесите Phi-3 модел

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изаберите Azure Machine Learning радни простор који сте креирали.

    ![Изаберите радни простор који сте креирали.](../../../../../../translated_images/sr/06-04-select-workspace.a92934ac04f4f181.webp)

1. Извршите следеће радње:

    - Изаберите **Model catalog** са левог менија.
    - Укуцајте *phi-3-mini-4k* у **претрази** и изаберите **Phi-3-mini-4k-instruct** из понуђених опција.

    ![Укуцајте phi-3-mini-4k.](../../../../../../translated_images/sr/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Изаберите **Fine-tune** из навигационог менија.

    ![Изаберите фино подешавање.](../../../../../../translated_images/sr/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Извршите следеће радње:

    - Изаберите **Select task type** на **Chat completion**.
    - Изаберите **+ Select data** да бисте отпремили **Тренинг податке**.
    - Изаберите тип отпремања валидирајућих података на **Provide different validation data**.
    - Изаберите **+ Select data** да бисте отпремили **Валидирајуће податке**.

    ![Попуните страницу за фино подешавање.](../../../../../../translated_images/sr/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Можете изабрати **Advanced settings** да прилагодите конфигурације као што су **learning_rate** и **lr_scheduler_type** за оптимизацију процеса фино подешавања у складу са вашим специфичним потребама.

1. Изаберите **Finish**.

1. У овој вежби сте успешно фино подесили Phi-3 модел користећи Azure Machine Learning. Имајте на уму да процес фино подешавања може трајати знатно време. Након покретања посла фино подешавања, морате сачекати да се заврши. Статус посла можете пратити тако што ћете отићи на картицу Jobs са леве стране вашег Azure Machine Learning Workspace-а. У следећој серији, распоређиваћете фино подешени модел и интегрисати га са Prompt flow.

    ![Погледајте посао фино подешавања.](../../../../../../translated_images/sr/06-08-output.2bd32e59930672b1.webp)

### Распоредите фино подешени Phi-3 модел

Да бисте интегрисали фино подешени Phi-3 модел са Prompt flow, потребно је да распоредите модел како би био доступан за реално време предикције. Овај процес подразумева регистрацију модела, креирање онлајн крајње тачке и распоређивање модела.

У овој вежби ћете:

- Регистровати фино подешени модел у Azure Machine Learning радном простору.
- Креирати онлајн крајњу тачку.
- Распоредити регистровани фино подешени Phi-3 модел.

#### Региструјте фино подешени модел

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изаберите Azure Machine Learning радни простор који сте креирали.

    ![Изаберите радни простор који сте креирали.](../../../../../../translated_images/sr/06-04-select-workspace.a92934ac04f4f181.webp)

1. Изаберите **Models** са левог менија.
1. Изаберите **+ Register**.
1. Изаберите **From a job output**.

    ![Региструјте модел.](../../../../../../translated_images/sr/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Изаберите посао који сте креирали.

    ![Изаберите посао.](../../../../../../translated_images/sr/07-02-select-job.3e2e1144cd6cd093.webp)

1. Изаберите **Next**.

1. Изаберите **Model type** на **MLflow**.

1. Уверите се да је изабран **Job output**; то би требало бити аутоматски изабрано.

    ![Изаберите излаз.](../../../../../../translated_images/sr/07-03-select-output.4cf1a0e645baea1f.webp)

2. Изаберите **Next**.

3. Изаберите **Register**.

    ![Изаберите региструј.](../../../../../../translated_images/sr/07-04-register.fd82a3b293060bc7.webp)

4. Можете погледати ваш регистровани модел тако што ћете отићи у мени **Models** са леве стране.

    ![Регистровани модел.](../../../../../../translated_images/sr/07-05-registered-model.7db9775f58dfd591.webp)

#### Распоредите фино подешени модел

1. Идите у Azure Machine Learning радни простор који сте креирали.

1. Изаберите **Endpoints** са левог менија.

1. Изаберите **Real-time endpoints** из навигационог менија.

    ![Креирајте крајњу тачку.](../../../../../../translated_images/sr/07-06-create-endpoint.1ba865c606551f09.webp)

1. Изаберите **Create**.

1. Изаберите регистровани модел који сте креирали.

    ![Изаберите регистровани модел.](../../../../../../translated_images/sr/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Изаберите **Select**.

1. Извршите следеће радње:

    - Изаберите **Virtual machine** на *Standard_NC6s_v3*.
    - Изаберите број инстанци које желите да користите. На пример, *1*.
    - Изаберите опцију **Endpoint** на **New** да бисте креирали нову крајњу тачку.
    - Унесите име крајње тачке. Мора бити јединствено.
    - Унесите име распореда. Мора бити јединствено.

    ![Попуните подешавања распореда.](../../../../../../translated_images/sr/07-08-deployment-setting.43ddc4209e673784.webp)

1. Изаберите **Deploy**.

> [!WARNING]
> Да бисте избегли додатне трошкове на вашем налогу, обавезно избришите креирану крајњу тачку у Azure Machine Learning радном простору.
>

#### Провера статуса распореда у Azure Machine Learning радном простору

1. Идите у Azure Machine Learning радни простор који сте креирали.

1. Изаберите **Endpoints** са левог менија.

1. Изаберите крајњу тачку коју сте креирали.

    ![Изаберите крајње тачке](../../../../../../translated_images/sr/07-09-check-deployment.325d18cae8475ef4.webp)

1. На овој страници можете управљати крајњим тачкама током процеса распореда.

> [!NOTE]
> Кад распоред буде завршен, уверите се да је **Live traffic** подешен на **100%**. Ако није, изаберите **Update traffic** да прилагодите саобраћајна подешавања. Имајте на уму да не можете тестирати модел ако је саобраћај постављен на 0%.
>
> ![Подесите саобраћај.](../../../../../../translated_images/sr/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Сценарио 3: Интеграција са Prompt flow и ћаскање са вашим прилагођеним моделом у Microsoft Foundry

### Интегришите прилагођени Phi-3 модел са Prompt flow

Након што сте успешно распоредили ваш фино подешени модел, сада га можете интегрисати са Prompt Flow да бисте користили модел у реалној апликацији, омогућавајући разне интерактивне задатке са вашим прилагођеним Phi-3 моделом.

У овој вежби ћете:

- Креирати Microsoft Foundry Hub.
- Креирати Microsoft Foundry пројекат.
- Креирати Prompt flow.
- Додати прилагођену везу за фино подешени Phi-3 модел.
- Подесити Prompt flow за ћаскање са вашим прилагођеним Phi-3 моделом.

> [!NOTE]
> Такође можете интегрисати са Promptflow коришћењем Azure ML Studio. Иста процедура интеграције може се применити у Azure ML Studio.

#### Креирајте Microsoft Foundry Hub

Пре него што креирате Пројекат, потребно је да креирате Hub. Hub делује као Ресурсна група, што вам омогућава да организујете и управљате више Пројеката унутар Microsoft Foundry.
1. Посетите [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Изаберите **All hubs** са картице са леве стране.

1. Изаберите **+ New hub** из навигационог менија.

    ![Create hub.](../../../../../../translated_images/sr/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Извршите следеће задатке:

    - Унесите **Hub name**. Мора бити јединствена вредност.
    - Изаберите вашу Azure **Subscription**.
    - Изаберите **Resource group** који желите да користите (направите нову ако је потребно).
    - Изаберите **Location** коју желите да користите.
    - Изаберите **Connect Azure AI Services** који желите да користите (направите нови ако је потребно).
    - Изаберите **Connect Azure AI Search** да бисте **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/sr/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Изаберите **Next**.

#### Креирање Microsoft Foundry Пројекта

1. У Hub-у који сте креирали, изаберите **All projects** са картице са леве стране.

1. Изаберите **+ New project** из навигационог менија.

    ![Select new project.](../../../../../../translated_images/sr/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Унесите **Project name**. Мора бити јединствена вредност.

    ![Create project.](../../../../../../translated_images/sr/08-05-create-project.4d97f0372f03375a.webp)

1. Изаберите **Create a project**.

#### Додавање прилагођене конекције за фино подешени Phi-3 модел

Да бисте интегрисали свој прилагођени Phi-3 модел са Prompt flow, потребно је да сачувате endpoint и кључ модела у прилагођеној конекцији. Ова конфигурација обезбеђује приступ вашем прилагођеном Phi-3 моделу у Prompt flow.

#### Поставите api кључ и endpoint URI фино подешеног Phi-3 модела

1. Посетите [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Идите до Azure Machine learning workspace који сте креирали.

1. Изаберите **Endpoints** са картице са леве стране.

    ![Select endpoints.](../../../../../../translated_images/sr/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Изаберите endpoint који сте креирали.

    ![Select endpoints.](../../../../../../translated_images/sr/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Изаберите **Consume** из навигационог менија.

1. Копирајте ваш **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sr/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Додавање прилагођене конекције

1. Посетите [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Идите до Microsoft Foundry пројекта који сте креирали.

1. У пројекту који сте креирали, изаберите **Settings** са картице са леве стране.

1. Изаберите **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/sr/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Изаберите **Custom keys** из навигационог менија.

    ![Select custom keys.](../../../../../../translated_images/sr/08-10-select-custom-keys.856f6b2966460551.webp)

1. Извршите следеће задатке:

    - Изаберите **+ Add key value pairs**.
    - За име кључа унесите **endpoint** и залепите endpoint који сте копирали из Azure ML Studio у поље за вредност.
    - Поново изаберите **+ Add key value pairs**.
    - За име кључа унесите **key** и залепите кључ који сте копирали из Azure ML Studio у поље за вредност.
    - Након додавања кључева, означите **is secret** да бисте спречили откривање кључа.

    ![Add connection.](../../../../../../translated_images/sr/08-11-add-connection.785486badb4d2d26.webp)

1. Изаберите **Add connection**.

#### Креирање Prompt flow

Додали сте прилагођену конекцију у Microsoft Foundry. Сада, хајде да креирамо Prompt flow пратећи следеће кораке. Затим ћете повезати овај Prompt flow са прилагођеном конекцијом како бисте могли користити фино подешени модел унутар Prompt flow.

1. Идите до Microsoft Foundry пројекта који сте креирали.

1. Изаберите **Prompt flow** са картице са леве стране.

1. Изаберите **+ Create** из навигационог менија.

    ![Select Promptflow.](../../../../../../translated_images/sr/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Изаберите **Chat flow** из навигационог менија.

    ![Select chat flow.](../../../../../../translated_images/sr/08-13-select-flow-type.2ec689b22da32591.webp)

1. Унесите **Folder name** који желите да користите.

    ![Enter name.](../../../../../../translated_images/sr/08-14-enter-name.ff9520fefd89f40d.webp)

2. Изаберите **Create**.

#### Подешавање Prompt flow за разговор са вашим прилагођеним Phi-3 моделом

Потребно је да интегришете фино подешени Phi-3 модел у Prompt flow. Међутим, постојећи Prompt flow није дизајниран за ову сврху. Стога морате редизајнирати Prompt flow како бисте омогућили интеграцију прилагођеног модела.

1. У Prompt flow-у извршите следеће задатке да бисте преправили постојећи ток:

    - Изаберите **Raw file mode**.
    - Обришите сав постојећи код у фајлу *flow.dag.yml*.
    - Додајте следећи код у фајл *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Изаберите **Save**.

    ![Select raw file mode.](../../../../../../translated_images/sr/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Додајте следећи код у *integrate_with_promptflow.py* фајл да бисте користили прилагођени Phi-3 модел у Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Подешавање пријављивања
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" је назив прилагођене везе, "endpoint", "key" су кључеви у прилагођеној вези
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Пријави цео JSON одговор
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/sr/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> За детаљније информације о коришћењу Prompt flow у Microsoft Foundry, можете погледати [Prompt flow у Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изаберите **Chat input**, **Chat output** да омогућите разговор са вашим моделом.

    ![Input Output.](../../../../../../translated_images/sr/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Сада сте спремни да разговарате са својим прилагођеним Phi-3 моделом. У наредној вежби научићете како да покренете Prompt flow и користите га за разговор са вашим фино подешеним Phi-3 моделом.

> [!NOTE]
>
> Преправљени ток би требао да изгледа као на слици испод:
>
> ![Flow example.](../../../../../../translated_images/sr/08-18-graph-example.d6457533952e690c.webp)
>

### Разговарајте са својим прилагођеним Phi-3 моделом

Сада када сте фино подесили и интегрисали свој прилагођени Phi-3 модел са Prompt flow, спремни сте да почнете интеракцију са њим. Ова вежба ће вас провести кроз процес подешавања и покретања разговора са вашим моделом помоћу Prompt flow. Пратећи ове кораке, моћи ћете у потпуности да искористите могућности свог фино подешеног Phi-3 модела за разне задатке и разговоре.

- Разговарајте са својим прилагођеним Phi-3 моделом користећи Prompt flow.

#### Покретање Prompt flow

1. Изаберите **Start compute sessions** да покренете Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sr/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Изаберите **Validate and parse input** да освежите параметре.

    ![Validate input.](../../../../../../translated_images/sr/09-02-validate-input.317c76ef766361e9.webp)

1. Изаберите **Value** од **connection** која води до прилагођене конекције коју сте креирали. На пример, *connection*.

    ![Connection.](../../../../../../translated_images/sr/09-03-select-connection.99bdddb4b1844023.webp)

#### Разговор са вашим прилагођеним моделом

1. Изаберите **Chat**.

    ![Select chat.](../../../../../../translated_images/sr/09-04-select-chat.61936dce6612a1e6.webp)

1. Ево примера резултата: Сада можете разговарати са својим прилагођеним Phi-3 моделом. Препоручује се да постављате питања везана за податке који су коришћени за фино подешавање.

    ![Chat with prompt flow.](../../../../../../translated_images/sr/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Огрaнчење одговорности**:  
Овај документ је преведен коришћењем AI услуге за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако стремимо ка тачности, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала употребом овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
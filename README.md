# Формирование искусственной БД для обучения нейронной сети

**Формат продукта:**  
Икусственный датасет;  
Обученная нейронная сеть.  
<br>

**Команда:**  
ПроКомпетенции: №3303  
TeamProject: 21/ЛКП-1751-2021  
<br>  

**Цель:**  
Формирование искусственной БД для обучения нейронной сети с использованием игрового движка Unity. Тестирование простых моделей нейронных сетей на созданной БД.  
<br>  

**Опиcание:**  
В рамках данной работы проводится создание искусственной базы данных (датасета) с помощью игрового Движка Unity. В качестве опорной БД используется [UCSD Anomaly Detection Dataset](http://www.svcl.ucsd.edu/projects/anomaly/dataset.html). После формирования БД производится тестирование обучения нейронной сети на классической БД и на искусственной.  
В рамках работы проверяется гипотеза **о возможности искусственной генерации данных** для обучения нейронных сетей детектировать девиантное поведение.  
____
## Результаты работы 
### Создание датасета
* [Виртуальный датасет](https://disk.yandex.ru/d/8J9kPHXBkgxoqw)



-|Original  | Synthetic
----|------------- | -------------
ped1/train|![](Dataset analytics/orig_ped1_train003.gif)|![](Dataset analytics/virt_ped1_train003.gif)
ped1/test| ![](Dataset analytics/orig_ped1_test019.gif)|![](Dataset analytics/virt_ped1_test019.gif)
ped2/train|![](Dataset analytics/orig_ped2_train006.gif)|![](Dataset analytics/virt_ped2_train006.gif)
ped2/test|![](Dataset analytics/orig_ped2_test004.gif)|![](Dataset analytics/virt_ped2_test004.gif)
___
### Обучение нейронных сетей
* [Обученные нейронные сети]()  

Выборки| Результат
------------- | -------------
Оригинал + Оригинал | ![](Dataset analytics/originalOnOriginal.gif)
Синт. + Оригинал  | ![](Dataset analytics/ourOnOriginal.gif)
Выборки в таблце описаны в формате Train+Test
___
**Стек технологий:** 

Технология  | Применение в рамках проекта
------------- | -------------
Unity 3D  | Создание синтетического датасета
C#  | Написание скриптов для Unity
Python | Написание утилит вспомогательного характера
Jupiter Notebook | Работа с нейронными сетями

<br>
 
**Использованные архитектуры нейронных сетей:**
* Autoencoder 
* Spatio-Temporal Autoencoder with Convolutional LSTM
___

